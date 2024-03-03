import os
import boto3


class DynamoDBClient:
    def __init__(self):
        table_name = os.environ.get('DYNAMODB_TABLE_NAME')
        if not table_name:
            raise ValueError("Nome da tabela do DynamoDB não fornecido.")
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(self.table_name)

    def get_item_by_pk(self, pk):
        """
        Obtém um item do DynamoDB pelo valor da chave primária (PK).

        Args:
            pk (str): O valor da chave primária (PK).

        Returns:
            dict: O item obtido do DynamoDB, se encontrado. None caso contrário.
        """
        try:
            response = self.table.get_item(Key={'PK': pk})
            item = response.get('Item')
            return item
        except Exception as e:
            # Log da exceção, se necessário
            print(f"Erro ao obter item do DynamoDB: {e}")
            return None


# Criar uma instância global do cliente DynamoDB
dynamodb_client = DynamoDBClient()
