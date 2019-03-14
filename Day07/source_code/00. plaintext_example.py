
def save_to_plain_text(filename, data):
    with open(filename, 'w') as data_file:
        for key, value in data.items():
            data_file.write(
                f'{key}={value}\n'
            )

if __name__ == '__main__':
    from helpers import get_person

    luke = get_person(1)
    save_to_plain_text('luke.txt', luke)