# noqa

def minha_funcao(*args, **kwargs):
    print("Argumentos posicionais:")
    for arg in args:
        print(arg)
    print("\nArgumentos de palavra-chave:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Chamada da função com argumentos posicionais e de palavra-chave
minha_funcao(1, 2, 3, arg1="a", arg2="b", arg3="c")




###################################


def lambda_handler(event, context):
    nome = event.get('pathParameters', {}).get('nome', 'Desconhecido')
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': f'OBRIGADO {nome}'
    }


import unittest
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_lambda_handler_with_name(self):
        event = {
            'pathParameters': {
                'nome': 'João'
            }
        }
        expected_response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': 'OBRIGADO João'
        }
        self.assertEqual(lambda_handler(event, None), expected_response)

    def test_lambda_handler_without_name(self):
        event = {}
        expected_response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': 'OBRIGADO Desconhecido'
        }
        self.assertEqual(lambda_handler(event, None), expected_response)

if __name__ == '__main__':
    unittest.main()
