import sys
import requests


def main():
    # 명령줄 인자로부터 비트코인 수량 가져오기
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        print("Error: The number of bitcoins must be a number.")
        sys.exit(1)

    # CoinDesk API에서 비트코인 현재 가격 조회
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: Unable to retrieve data from CoinDesk API. {e}")
        sys.exit(1)

    # JSON 응답 파싱
    try:
        data = response.json()
        rate_float = data["bpi"]["USD"]["rate_float"]
    except (KeyError, ValueError, TypeError) as e:
        print(f"Error: Unexpected data format received from CoinDesk API. {e}")
        sys.exit(1)

    # 계산 및 출력
    try:
        total_cost = num_bitcoins * rate_float
        print(f"${total_cost:,.4f}")
    except Exception as e:
        print(f"Error: An unexpected error occurred during calculation or printing. {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
