def filter_model(model, query_params, custom_filters=None):
    fields = model._meta.get_fields()
    filters = {}
    for field in fields:
        if hasattr(field, 'attname'):
            query_filter = query_params.get(field.attname)
            if query_filter is not None:
                filters[field.attname] = query_filter
    if custom_filters is not None:
        custom_filters_parsed = {}
        for query_filter, query_param_candidate in custom_filters.items():
            query_param = query_params.get(query_param_candidate)
            if query_param is not None:
                custom_filters_parsed[query_filter] = query_param
        filters = {**filters, **custom_filters_parsed}
    objects = model.objects.filter(**filters)
    order = query_params.get('order_by')
    if order is not None:
        return objects.order_by(order)
    return objects
