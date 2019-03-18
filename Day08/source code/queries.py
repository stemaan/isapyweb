QUERY_MAP = {
    'all': 'select * from klienci;',
    'all_last_names': 'select nazwisko from klienci;',
    'find_by_name': 'select * from klienci where imie = "Adam";',
    'all_adresses': 'SELECT * FROM adresy;',
    'join_address': 'SELECT imie, nazwisko, adres, nazwa FROM klienci LEFT JOIN adresy ON klienci.id = adresy.klient_id;'
}
