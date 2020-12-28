def get_messages_400_locoal(variable):
    data = {
           'status': 400,
           'existe': False,
           'title':  variable.capitalize(),
           'estado': 'warning',
           'message': format(variable)
            }
    return data