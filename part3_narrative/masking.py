def alias_for(reseller_id):
    return f"ALIAS-{reseller_id[3:]}"


def assert_no_raw_names_leak(text, reseller_names):
    for name in reseller_names:
        if name in text:
            return False
    return True