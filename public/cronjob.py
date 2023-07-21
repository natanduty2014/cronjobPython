import schedule
import time
import threading
import subprocess
# Script 1 - Tarefa que será executada a cada 10 segundos
def script1():
    print("Executando Script 1...")
    try:
        bashCommand = "php /var/www/html/meu_script.php"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)
    except Exception as e:
        print(e)
# Script 2 - Tarefa que será executada a cada 20 segundos
def script2():
    print("Executando Script 2...")

# Script 3 - Tarefa que será executada a cada 30 segundos
def script3():
    print("Executando Script 3...")

# Script 4 - Tarefa que será executada a cada minuto
def script4():
    print("Executando Script 4...")

# Agende as tarefas para serem executadas em intervalos diferentes
schedule.every(10).seconds.do(script1)
schedule.every(20).seconds.do(script2)
schedule.every(30).seconds.do(script3)
schedule.every(1).minutes.do(script4)

# Função para executar o agendamento em threads separadas
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Crie uma lista de threads para cada script e inicie as threads
threads = [
    threading.Thread(target=run_schedule) for _ in range(1)
]

# Inicie as threads
for thread in threads:
    thread.start()

# Espere até que todas as threads sejam concluídas
for thread in threads:
    thread.join()
