import polars as pl

from datetime import datetime
from pathlib import Path

from myapp.email import send_main
from myapp.template import TemplateWorker

source = Path.cwd() / "examples" / "data.xlsx"
template = TemplateWorker()

df = pl.read_excel(source.absolute().as_posix())

filter_df = df.filter(pl.col("Birthday") == datetime.now().date())

for row in filter_df.iter_rows(named=True):
    # print(row)
    name = row["Name"]
    email = row["Email"]
    send_main(
        subject="La multi ani " + name,
        to=email,
        body=template.render(
            receiver_name=name,
            sender_name="Python Team",
        ),
    )


# print(filter_df)
