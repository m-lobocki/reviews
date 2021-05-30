def merge_body_model(body, model):
    fields = model._meta.get_fields()
    change = False
    for field in fields:
        if hasattr(field, 'attname'):
            body_property = body.get(field.attname)
            if body_property is not None:
                setattr(model, field.attname, body_property)
                change = True
    if change:
        model.save()
    return model
