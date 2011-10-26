import docutils.core
import logging

config = {
    'name': "reStructuredText",
    'description': "Renders reStructuredText formatted text to HTML",
    'aliases': ['rst']
    }


def run(content):
    overrides = {'initial_header_level': 2}
    ret = docutils.core.publish_parts(content, writer_name='html4css1',
                                      settings_overrides=overrides)
    return ret['html_body']
