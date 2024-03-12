from datetime import datetime

from sample_package.sample_module import greeting


def main() -> None:
    print(greeting())
    print('Today is', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    main()
