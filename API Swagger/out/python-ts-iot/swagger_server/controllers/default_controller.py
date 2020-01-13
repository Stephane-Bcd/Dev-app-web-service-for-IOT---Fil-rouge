import connexion
import six

from swagger_server import util


def mean_sensor_id_get(sensor_id, start_date=None, end_date=None):  # noqa: E501
    """Calculer la moyenne d&#x27;un capteur entre deux dates

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param sensor_id: String Id of the sensor to get
    :type sensor_id: str
    :param start_date: Integer/timestamp of the start date
    :type start_date: int
    :param end_date: Integer/timestamp of the end date
    :type end_date: int

    :rtype: List[int]
    """
    return 'do some magic!'
