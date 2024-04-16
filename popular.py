import mysql.connector
from faker import Faker
import random
import municipios

fake = Faker('pt_BR')

num_registros = 100 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="mydb"
)

def adress():
    for _ in range(num_registros):
        street = fake.street_name()
        zip_code = fake.postcode()
        num = fake.building_number()
        City_id_city = random.randint(1,5313)
        mycursor.execute("INSERT INTO address(street, zip_code, number, City_id_city) VALUES(%s, %s, %s, %s)",(street, zip_code, num, City_id_city))

def result():
    for _ in range(num_registros):
        name = fake.word()
        mycursor.execute("INSERT INTO result(name) VALUES(%s)",(name,))

def client():
    for _ in range(num_registros):
        name = fake.name()
        cpf = fake.cpf()
        cnpj = fake.cnpj()
        company = fake.company()
        address_id_address = random.randint(1, num_registros)
        mycursor.execute("INSERT INTO client(name, cpf, cnpj, company, address_id_address) VALUES(%s, %s, %s, %s, %s)",(name, cpf, cnpj, company, address_id_address))

def contactEmail():
    for _ in range(num_registros):
        content = fake.email()
        typeC = "email"
        mycursor.execute("INSERT INTO contact(content, type) VALUES(%s, %s)",(content, typeC))

def contactPhone():
    for _ in range(num_registros):
        content = fake.phone_number()
        typeC = "phone"
        mycursor.execute("INSERT INTO contact(content, type) VALUES(%s, %s)",(content, typeC))

def client_contact():
    existing_entries = set()

    mycursor.execute("SELECT Client_id_client, Contact_id_contact FROM client_contact")
    for row in mycursor.fetchall():
        existing_entries.add((row[0], row[1]))

    for _ in range(num_registros):
        while True:
            Client_id_client = random.randint(1, num_registros)
            Contact_id_contact = random.randint(1, num_registros)
            if (Client_id_client, Contact_id_contact) not in existing_entries:
                break
        mycursor.execute("INSERT INTO client_contact(Client_id_client, Contact_id_contact) VALUES(%s, %s)", (Client_id_client, Contact_id_contact))
        existing_entries.add((Client_id_client, Contact_id_contact))

def role():
    for _ in range(num_registros):
        name = fake.job()
        mycursor.execute("INSERT INTO role(name) VALUES(%s)",(name,))

def statusUser():
    for _ in range(num_registros):
        name = fake.word()
        typeS = "user"
        mycursor.execute("INSERT INTO status(name, type) VALUES(%s, %s)",(name, typeS))

def statusOffer():
    for _ in range(num_registros):
        name = fake.word()
        typeS = "offer"
        mycursor.execute("INSERT INTO status(name, type) VALUES(%s, %s)",(name, typeS))

def team():
    for _ in range(num_registros):
        name = fake.company()
        mycursor.execute("INSERT INTO team(name) VALUES(%s)",(name,))

def user():
    for _ in range(num_registros):
        name = fake.name()
        email = fake.email()
        confirmedEMail = email
        phone = fake.phone_number()
        image_key = fake.word()
        created_at = fake.date_time_this_decade()
        role_id_role = random.randint(1, num_registros)
        status_id_status = random.randint(1, num_registros)
        team_id_team = random.randint(1, num_registros)
        mycursor.execute("INSERT INTO user(name, email, confirmed_email, phone, image_key, created_at, role_idrole, status_idstatus, team_id_team) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(name, email, confirmedEMail, phone, image_key, created_at, role_id_role, status_id_status, team_id_team))

def offer():
    for _ in range(num_registros):
        service = fake.word()
        offer_date = fake.date_time_this_decade()
        value = random.uniform(1.20, 1000.20)
        description = fake.text()
        file_key = fake.word()
        status_id_status = random.randint(1, num_registros)
        user_id_user = random.randint(1, num_registros)
        mycursor.execute("INSERT INTO offer(service, offer_date, value, description, file_key, status_id_status, user_id_user) VALUES(%s, %s, %s, %s, %s, %s, %s)",(service, offer_date, value, description, file_key, status_id_status, user_id_user))

def call():
    for _ in range(num_registros):
        contact = fake.phone_number()
        date = fake.date_time_this_decade()
        description = fake.text()
        duration = random.uniform(1.20, 1000.20)
        offer_id_offer = random.randint(1, num_registros)
        client_id_client = random.randint(1, num_registros)
        result_id_result = random.randint(1, num_registros)
        mycursor.execute("INSERT INTO `call`(contact, description, date, duration, offer_id_offer, client_id_client, result_idresult) VALUES(%s, %s, %s, %s, %s, %s, %s)",(contact, description, date, duration, offer_id_offer, client_id_client, result_id_result))

def goal():
    for _ in range(num_registros):
        description = fake.text()
        deadline = fake.date_time_this_decade()
        target_value = random.uniform(1.20, 1000.20)
        current_value = random.uniform(1.20, 1000.20)
        id_user_responsible = random.randint(1, num_registros)
        mycursor.execute("INSERT INTO goal(description, deadline, target_value, current_value, id_user_responsible) VALUES(%s, %s, %s, %s, %s)",(description, deadline, target_value, current_value, id_user_responsible))

def priority():
    for _ in range(num_registros):
        name = fake.word()
        mycursor.execute("INSERT INTO priority(name) VALUES(%s)",(name,))

def activity():
    for _ in range(num_registros):
        start_date = fake.date_time_this_decade()
        end_date = fake.date_time_this_decade()
        description = fake.text()
        priority_id_priority = random.randint(1, num_registros)
        team_id_team = random.randint(1, num_registros)
        mycursor.execute("INSERT INTO activity(start_date, end_date, description, priority_id_priority, team_id_team) VALUES(%s, %s, %s, %s, %s)",(start_date, end_date, description, priority_id_priority, team_id_team))

def estado():
    for estado, uf in estados_brasil.items():
        mycursor.execute("INSERT INTO state(name, uf) VALUES(%s, %s)", (estado, uf,))

def status():
    for status in status_proposta:
        mycursor.execute("INSERT INTO status(name) VALUES(%s)", (status,))

def municipios_func(municipios):
    for municipio, idEstado in municipios.items():
        mycursor.execute("INSERT INTO city(name, state_id_state) VALUES(%s, %s)",(municipio, idEstado,))

estados_brasil = {
    "Acre": "AC", "Alagoas": "AL", "Amapá": "AP", "Amazonas": "AM", "Bahia": "BA", "Ceará": "CE",
    "Distrito Federal": "DF", "Espírito Santo": "ES", "Goiás": "GO", "Maranhão": "MA",
    "Mato Grosso": "MT", "Mato Grosso do Sul": "MS", "Minas Gerais": "MG", "Pará": "PA",
    "Paraíba": "PB", "Paraná": "PR", "Pernambuco": "PE", "Piauí": "PI", "Rio de Janeiro": "RJ",
    "Rio Grande do Norte": "RN", "Rio Grande do Sul": "RS", "Rondônia": "RO", "Roraima": "RR",
    "Santa Catarina": "SC", "São Paulo": "SP", "Sergipe": "SE", "Tocantins": "TO"
}

mycursor = mydb.cursor()


status_proposta = [
    "Negociação", "Parado", "Fechado", "Acompanhar"
]



#Estados
estado()

#Cidades
municipios_func(municipios.municipios)

#Endereços
adress()

#Clientes
client()

#Contatos
contactEmail()
contactPhone()

#Clientes Contatos
client_contact()

#Funções
role()

#Status Usuário
statusUser()

#Status Proposta
statusOffer()

#Equipes
team()

#Usuários
user()

#Propostas
offer()

#Resultados
result()

#Ligações
call()

#Metas
goal()

#Prioridades
priority()

#Atividades
activity()

mydb.commit()
mydb.close()