import requests
import time
import sys

def test_load_balancer():
    print("=== Teste do Load Balancer ===")
    print("Fazendo requisições para o NGINX...")
    print("=" * 50)
    
    responses = {}
    
    for i in range(20):
        try:
            response = requests.get('http://localhost:80')
            container_name = response.text.strip()
            
            if container_name in responses:
                responses[container_name] += 1
            else:
                responses[container_name] = 1
            
            print(f"Requisição {i+1:2d}: {container_name}")
            time.sleep(0.3)
            
        except requests.exceptions.ConnectionError:
            print(f"Requisição {i+1:2d}: ERRO - Serviço indisponível")
            print("Aguarde os containers inicializarem e tente novamente.")
            break
        except Exception as e:
            print(f"Requisição {i+1:2d}: ERRO - {e}")
            break
    
    print("=" * 50)
    print("=== Estatísticas ===")
    for container, count in responses.items():
        print(f"{container}: {count} requisições")
    
    total = sum(responses.values())
    print(f"\nTotal de requisições bem-sucedidas: {total}")

if __name__ == "__main__":
    test_load_balancer()