def clicky_anonymize(request):
    # see https://clicky.com/help/custom
    return {
        'clicky_cookies_disable': 1,
        # no popups, no consent
        'clicky_visitor_consent': 0,
    }
