def filter_model(model, query_params):
    fields = model._meta.get_fields()
    filters = {}
    for field in fields:
        if hasattr(field, 'attname'):
            query_filter = query_params.get(field.attname)
            if query_filter is not None:
                filters[field.attname] = query_filter
    objects = model.objects.filter(**filters)
    order = query_params.get('order_by')
    if order is not None:
        return objects.order_by(order)
    return objects
