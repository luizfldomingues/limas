import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def hourly_report(sales_per_hour):
    hour_sales = dict()
    for sales in sales_per_hour:
        hour_sales.update({
            int(sales["hour"]): sales["sold"],
        })
    fhour, lhour = min(hour_sales.keys()), max(hour_sales.keys())
    hours = range(int(fhour), int(lhour)+1)
    sales = list()
    print(hour_sales)
    for hour in hours:
        if hour_sales.get(hour):
            sales.append(hour_sales.get(hour)/100)
        else:
            sales.append(0)
    
    fig, ax = plt.subplots()
    #ax.plot(hours, sales)

    # Set the major x-axis ticks to be integers

    print(hours, sales)
    #plt.figure()
    plt.plot(hours, sales)
    plt.bar(hours,sales)

    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.title("Vendas por hora")
    plt.xlabel("Hora")
    plt.ylabel("Total em Reais")
    plt.show()
