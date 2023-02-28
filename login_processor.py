import json
import psycopg2

# Connect to Postgres
postgres_conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='postgres',
    user='postgres',
    password='postgres'
)

# Receive messages from a local message queue
queue = [{'user_id': '1234', 'device_id': 'abcd1234', 'ip': '192.168.1.1', 'app_version': '1.0', 'device_type': 'phone', 'locale': 'en', 'create_date': '2022-01-01T00:00:00Z'},         {'user_id': '5678', 'device_id': 'efgh5678', 'ip': '192.168.1.2', 'app_version': '2.0', 'device_type': 'tablet', 'locale': 'fr', 'create_date': '2022-01-02T00:00:00Z'},         {'user_id': '9012', 'device_id': 'ijkl9012', 'ip': '192.168.1.3', 'app_version': '3.0', 'device_type': 'phone', 'locale': 'de', 'create_date': '2022-01-03T00:00:00Z'}]

while len(queue) > 0:
    message = queue.pop(0)
    body = message

    # Mask device_id and ip
    masked_device_id = 'MASKED-' + body['device_id'][-4:]
    masked_ip = 'MASKED-' + body['ip'].split('.')[-1]
    body['masked_device_id'] = masked_device_id
    body['masked_ip'] = masked_ip
    del body['device_id']
    del body['ip']

    # Flatten JSON object
    user_id = body['user_id']
    app_version = int(float(body['app_version']))
    device_type = body['device_type']
    locale = body['locale']
    create_date = body['create_date']
    masked_device_id = body['masked_device_id']
    masked_ip = body['masked_ip']

    # Insert into Postgres
    with postgres_conn.cursor() as cur:
        cur.execute(
            'INSERT INTO user_logins VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
        )

    postgres_conn.commit()

print('No messages in queue')
