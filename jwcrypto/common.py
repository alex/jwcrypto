# Copyright (C) 2015 JWCrypto Project Contributors - see LICENSE file

from base64 import urlsafe_b64encode, urlsafe_b64decode


# Padding stripping versions as described in
# draft-ietf-jose-json-web-signature-41 appendix C


def base64url_encode(payload):
    return urlsafe_b64encode(payload).rstrip('=')


def base64url_decode(payload):
    l = len(payload) % 4
    if l == 2:
        payload += '=='
    elif l == 3:
        payload += '='
    elif l != 0:
        raise ValueError('Invalid base64 string')
    return urlsafe_b64decode(payload)


class InvalidJWAAlgorithm(Exception):
    def __init__(self, message=None):
        msg = 'Invalid JWS Algorithm name'
        if message:
            msg += ' (%s)' % message
        super(InvalidJWAAlgorithm, self).__init__(msg)
