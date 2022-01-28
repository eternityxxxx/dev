import json

import nsq
from marshmallow import Schema, fields


class MessageSchema(Schema):
    user = fields.Str()
    origin = fields.Str()
    destination = fields.Str()


def handler(message):
    schema = MessageSchema()

    try:
        result = schema.loads(message.data.decode())
        print(result)
    except json.JSONDecodeError:
        return False

    return True


r = nsq.Reader(
    message_handler=handler,
    nsqd_tcp_addresses=['127.0.0.1:4150'],
    topic='topic',
    channel='channel',
    lookupd_poll_interval=15,
)


if __name__ == '__main__':
    nsq.run()
