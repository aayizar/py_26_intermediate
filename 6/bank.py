from error.WifiConnectionException import WifiConnectionException

def qr_transaction(money):
    try:
        print('All done')
        raise WifiConnectionException('Wifi not found')
    except ArithmeticError as e:
        print(e)
        ...
        ...
        ...
    except WifiConnectionException as e:
        raise WifiConnectionException(f"In function qr_transaction have unknown error: {e}")


def transaction(transaction_type, money):
    try:
        if transaction_type == 'qr':
            qr_transaction(money)
            return True
        elif transaction_type == 'tranfer':
            ...
    except WifiConnectionException as e:
        print(e)
        ...