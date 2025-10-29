import base64
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def hourly_report(sales_per_hour):
    if not sales_per_hour:
        return None
    hour_sales = dict()
    for sales in sales_per_hour:
        hour_sales.update(
            {
                int(sales["hour"]): sales["sold"],
            }
        )
    fhour, lhour = min(hour_sales.keys()), max(hour_sales.keys())
    hours = range(int(fhour), int(lhour) + 1)
    sales = list()
    for hour in hours:
        if hour_sales.get(hour):
            sales.append(hour_sales.get(hour) / 100)
        else:
            sales.append(0)

    fig, ax = plt.subplots()

    plt.bar(hours, sales)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.title("Vendas por hora", fontsize=20, fontweight=600)
    plt.xlabel("Hora", fontsize=15)
    plt.ylabel("Total em Reais", fontsize=15)

    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")

    return data
