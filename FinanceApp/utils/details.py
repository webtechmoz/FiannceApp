users = {
    '1': {
        'name': 'Web Tech',
        'user': 'webtech',
        'email': 'webtech@email.com'
    },
    '2': {
        'name': 'Alex Zunguze',
        'user': 'azunguze',
        'email': 'azunguze@email.com'
    },
}

balance = {
    users['1']['user']: 2500.95,
    users['2']['user']: 3800.89
}

moviments = {
    users['1']['user']: {
        '0': 1890.85,
        '1': 950.99
    },
    users['2']['user']: {
        '0': 3999.99,
        '1': 1200.00
    }
}

extract = {
    users['1']['user']: {
        '1': {
            'data': '14/08/2024',
            'descrição': 'Recebimento de salários',
            'montante': 10900.95,
            'tipo': '0'
        },
        '2': {
            'data': '15/08/2024',
            'descrição': 'Conta de luz',
            'montante': 1000,
            'tipo': '1'
        },
        '3': {
            'data': '15/08/2024',
            'descrição': 'Comissão de venda',
            'montante': 3000,
            'tipo': '0'
        },
        '4': {
            'data': '16/08/2024',
            'descrição': 'Conta de água',
            'montante': 999.25,
            'tipo': '1'
        },
        '5': {
            'data': '20/08/2024',
            'descrição': 'Refeição',
            'montante': 800.70,
            'tipo': '1'
        }
    },
    users['2']['user']: {
        '1': {
            'data': '01/08/2024',
            'descrição': 'Prestação de serviços',
            'montante': 7800.95,
            'tipo': '0'
        },
        '2': {
            'data': '15/08/2024',
            'descrição': 'Conta de água',
            'montante': 1500,
            'tipo': '1'
        },
        '3': {
            'data': '10/08/2024',
            'descrição': 'Compra de aparelhos de som',
            'montante': 1600,
            'tipo': '1'
        },
        '4': {
            'data': '12/08/2024',
            'descrição': 'Conta de luz',
            'montante': 999.25,
            'tipo': '1'
        },
        '5': {
            'data': '20/08/2024',
            'descrição': 'Cinema',
            'montante': 1600.82,
            'tipo': '1'
        }
    }
}

buttons = {
    'pagar': {
        'icon': 'PAYMENT',
        'title': 'Pagar'
    },
    'receber': {
        'icon': 'MONEY',
        'title': 'Receber'
    },
    'transferir': {
        'icon': 'SEND',
        'title': 'Transferir'
    },
    'solicitar': {
        'icon': 'PAID',
        'title': 'Solicitar'
    }
}