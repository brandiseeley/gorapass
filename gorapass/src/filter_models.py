
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
    def filter_data(cls, data_models, filters):
        for selector in filters:
            attribute = selector[ModelFilter.ATTRIBUTE_NAME]
            value = selector[ModelFilter.ATTRIBUTE_VALUE]
            match selector[ModelFilter.FILTER_TYPE]:
                case 'exact':
                    data_models = [ record
                                    for record in data_models
                                    if getattr(record, attribute) == value ]
                case 'partial':
                    data_models = [ record
                                    for record in data_models
                                    if value.lower() in str(getattr(record, attribute)).lower() ]
                case 'less_than':
                    data_models = [ record
                                    for record in data_models
                                    if getattr(record, attribute) < value ]
                case 'greater_than':
                    data_models = [ record
                                    for record in data_models
                                    if getattr(record, attribute) > value ]
                case _:
                    pass
            # Return early if we run out of matching records
            if len(data_models) == 0:
                return data_models

        return data_models

    @classmethod
    def validate_selectors(cls, data_models, selectors):
        if not selectors:
            return { 'success': False,
                     'message': 'No selectors provided' }
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

            # Check that the attribute name exists on data model
            attribute_name = selector[ModelFilter.ATTRIBUTE_NAME]
            if not hasattr(data_models, attribute_name):
                return {
                    'success': False,
                    'message': f'Attribute: "{attribute_name}" does not exist on the data model',
                    }

            # Check that the filter type exists
            filter_type = selector[ModelFilter.FILTER_TYPE]
            if not filter_type in ModelFilter.FILTER_TYPES:
                return {
                    'success': False,
                    'message': f'Filter type "{filter_type}" does not exist',
                }

        return { 'success': True }
