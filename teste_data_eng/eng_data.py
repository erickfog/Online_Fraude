import json
import hashlib
from datetime import datetime

# Função para converter endereço IP em hash MD5
def hash_ip(ip):
    return hashlib.md5(ip.encode()).hexdigest()

def clean_string(string):
    # Remove as aspas extras e os caracteres de escape
    cleaned_string = string.strip('"\\')
    return cleaned_string
# Função para converter a data para formato UNIX timestamp

def convert_to_unix_timestamp(date_str):
    try:
        # Tenta converter a data usando o formato padrão
        return datetime.strptime(date_str, "%d/%b/%Y %H:%M:%S").timestamp()
    except ValueError:
        # Tenta ajustar para segundos com apenas um dígito
        return datetime.strptime(date_str[:-6] + date_str[-5:], "%d/%b/%Y %H:%M:%S").replace(second=int(date_str[-2:])).timestamp()

       

# Função para ler o arquivo de log e extrair os dados
def extract_data_from_log(log_file):
    data = []
    with open(log_file, 'r') as f:
        for line in f:
            parts = line.split()
            remote_host = parts[0]
            user_identity = parts[1]
            username = parts[2]
            date = convert_to_unix_timestamp(parts[3][1:] + ' ' + parts[4][:-1])
            request = parts[6] + ' ' + parts[7] + ' ' + parts[8]
            status_code = parts[9]
            response_time = parts[10]
            referer = parts[11]
            user_agent = ' '.join(parts[12:])
            data.append({
                'remote_host': remote_host,
                'user_identity': user_identity,
                'username': username,
                'date': date,
                'request': clean_string(request),
                'status_code': status_code,
                'response_time': response_time,
                'referer': clean_string(referer),
                'user_agent': clean_string(user_agent)
            })
    return data

def original_extract_data_from_log(log_file):
    data = []
    with open(log_file, 'r') as f:
        for line in f:
            parts = line.split()
            remote_host = parts[0]
            user_identity = parts[1]
            username = parts[2]
            date = parts[3][1:]  # Mantém a data como está
            request = ' '.join(parts[6:9])
            status_code = parts[9]
            response_time = parts[10]
            referer = parts[11]
            user_agent = ' '.join(parts[12:])
            data.append({
                'remote_host': remote_host,
                'user_identity': user_identity,
                'username': username,
                'date': date,
                'request': clean_string(request),
                'status_code': status_code,
                'response_time': response_time,
                'referer': clean_string(referer),
                'user_agent': clean_string(user_agent)
            })
    return data


# Função para escrever dados em formato JSON
def write_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# Função para encontrar os 10 maiores tempos de resposta com sucesso para a chamada GET /manual/
def find_top_10_slowest_requests(data):
    filtered_data = [d for d in data if d['status_code'] == '200' and d['referer'] ==  "http://localhost/svnview?repos=devel&rev=latest&root=SVNview/tmpl&list_revs=1"]
    sorted_data = sorted(filtered_data, key=lambda x: float(x['response_time']), reverse=True)
    return sorted_data[:10]

# Função para agrupar e contar solicitações por dia do ano.
def count_requests_per_day(log_file):
    data = original_extract_data_from_log(log_file)
    requests_per_day = {}
    for d in data:
        # Obtém a data no formato 'DD/MM/YYYY'
        date = d['date']
        if date in requests_per_day:
            # Se a data já existe no dicionário, aumente o contador de solicitações para esse dia
            requests_per_day[date] += 1
        else:
            # Se a data ainda não existe no dicionário, adicione-a com um contador de 1
            requests_per_day[date] = 1
    return requests_per_day



# Função para encontrar IPs únicos e suas últimas datas de solicitação.
def find_unique_ips_with_last_date(data):
    unique_ips = {}
    for d in data:
        ip = d['remote_host']
        date = d['date']
        unique_ips[ip] = max(unique_ips.get(ip, 0), date)
    return {ip: datetime.utcfromtimestamp(last_date).strftime('%Y-%m-%d %H:%M:%S') for ip, last_date in unique_ips.items()}

# Arquivo de log de entrada
log_file = 'test-access-001-05-seed-2.log'

# Vamos utilizar a função construída e extrair os dados do log
data = extract_data_from_log(log_file)

# Vamos escrever a saída em formato JSON
write_json(data, 'log_data.json')

# vamos encontrar os 10 maiores tempos de resposta com sucesso para a chamada GET /manual/
top_10_slowest_requests = find_top_10_slowest_requests(data)
write_json(top_10_slowest_requests, 'top_10_slowest_requests.json')

#Vamos contar solicitações por dia do ano
requests_per_day = count_requests_per_day(log_file)
write_json(requests_per_day, 'requests_per_day.json')

# Vamos encontrar IPs únicos e suas últimas datas de solicitação
unique_ips_with_last_date = find_unique_ips_with_last_date(data)
with open('unique_ips_with_last_date.txt', 'w') as f:
    for ip, last_date in unique_ips_with_last_date.items():
        f.write(f'{ip} - Last Date: {last_date}\n')

# Vamos escrever o log formatado com a data em formato UNIX timestamp e IP convertido em hash MD5
with open('formatted_access.log', 'w') as f:
    for d in data:
        formatted_date = datetime.utcfromtimestamp(d['date']).strftime('%Y-%m-%d %H:%M:%S')
        formatted_ip = hash_ip(d['remote_host'])
        f.write(f"{formatted_ip} - - [{formatted_date}] \"{d['request']}\" {d['status_code']} {d['response_time']} \"{d['referer']}\" \"{d['user_agent']}\"\n")
