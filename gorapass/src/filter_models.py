from gorapass.models import Hikes

class ModelFilter:
    ATTRIBUTE_NAME = 'attribute_name'
    ATTRIBUTE_VALUE = 'attribute_value'
    FILTER_TYPE = 'filter_type'

    SELECTOR_KEYS = {
        ATTRIBUTE_NAME,
        ATTRIBUTE_VALUE,
        FILTER_TYPE,
    }

    FILTER_TYPES = { 'exact', 'partial', 'less_than', 'greater_than' }

    @classmethod
    def filter_hikes(cls, hike_models, filters):
        for selector in filters:
            attribute = selector[ModelFilter.ATTRIBUTE_NAME]
            value = selector[ModelFilter.ATTRIBUTE_VALUE]
            match selector[ModelFilter.FILTER_TYPE]:
                case 'exact':
                    hike_models = [ hike
                                    for hike in hike_models
                                    if getattr(hike, attribute) == value ]
                case 'partial':
                    hike_models = [ hike
                                    for hike in hike_models
                                    if value.lower() in str(getattr(hike, attribute)).lower() ]
                case 'less_than':
                    hike_models = [ hike
                                    for hike in hike_models
                                    if getattr(hike, attribute) < value ]
                case 'greater_than':
                    hike_models = [ hike
                                    for hike in hike_models
                                    if getattr(hike, attribute) > value ]
                case _:
                    pass
            # Return early if we run out of matching hikes
            if len(hike_models) == 0:
                return hike_models

        return hike_models

    @classmethod
    def validate_hike_selectors(cls, selectors):
        for selector in selectors:

            # Check that the keys for the selector object are correct
            if set(selector.keys()) != ModelFilter.SELECTOR_KEYS:
                expected = ModelFilter.SELECTOR_KEYS
                actual = set(selector.keys())
                message = f'Selector objects must include attributes {expected}, not {actual}'

                return {
                    'success': False,
                    'message': message,
                    }

            # Check that the attribute name exists on hikes
            attribute_name = selector[ModelFilter.ATTRIBUTE_NAME]
            if not hasattr(Hikes, attribute_name):
                return {
                    'success': False,
                    'message': f'Attribute: "{attribute_name}" does not exist on Hikes models',
                    }
    
            # Check that the filter type exists
            filter_type = selector[ModelFilter.FILTER_TYPE]
            if not filter_type in ModelFilter.FILTER_TYPES:
                return {
                    'success': False,
                    'message': f'Filter type "{filter_type}" does not exist',
                }

        return { 'success': True }
