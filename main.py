#para importar usamos o import
import pandas as pd
from twilio.rest import Client
# Your Account SID and Auth Token from console.twilio.com
account_sid = "AC2fde6026e2e09c63a04ccbe139f40aff"
auth_token  = "0a185d65b8a64aebeaa079b5fd3341af"
client = Client(account_sid, auth_token)

list_meses = ['janeiro','fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in list_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[ tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas =  tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f"no mês {mes} alguém bateu a meta. Vendedor: {vendedor} , vendas: {vendas}")
        message = client.messages.create(
            to="+5551995321989",
            from_="+12707176437",
            body=(f"no mês {mes} alguém bateu a meta. Vendedor: {vendedor} , vendas: {vendas}"))
        print(message.sid)











