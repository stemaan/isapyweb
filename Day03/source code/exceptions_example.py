# przykład wykorzystania modułu logging
# sprawdzenie listy wyjątków w module requests.exceptions

import logging
import requests

# założenie podstawowego loggera piszącego do pliku exceptions_example.log
logging.basicConfig(filename='exceptions_example.log',level=logging.DEBUG)

# przykład obsługi dla odpowiedzi HTTP 200 i 401
for code in 200, 401:
    response = requests.get('https://httpstat.us/%s' % code)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as exc:
        logging.exception(exc)

    logging.debug('-'*120)

