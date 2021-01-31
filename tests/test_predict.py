import math

from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset


def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name='test.csv')
    single_test_json = test_data[0:1].to_json(orient='records')

    # When
    subject = make_prediction(input_data=single_test_json)

    # Then
    # On test si la fonction de prediction renvoie une valeur	
    assert subject is not None

    # Ensuite on test que la valeur retournée est bien un float
    assert isinstance(subject.get('predictions')[0], float)

    # Enfin on test selon notre exemple connu que la valeur retournée arrondi au supérieur est bien 112476
    assert math.ceil(subject.get('predictions')[0]) == 112476
