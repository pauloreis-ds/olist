from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error


def evaluation(y_true, y_pred, show_results=True):
    mae = mean_absolute_error(y_true, y_pred).round(2)
    mape = mean_absolute_percentage_error(y_true, y_pred) * 100
    if show_results:
        print(f'''On average, our predictions are {mape.round(2)}% above or below the real value.''')
        print(f'''Which means an error of about R$ {mae}''')
    return mae, mape
