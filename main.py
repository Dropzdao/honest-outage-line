line = "I'm the agent on duty and I can't reach any of our servers, so I can't confirm the cause or an ETA. I'll update this page as soon as I can verify anything."


def validate(text):
    assert len(text) <= 200, "entry line too long"
    assert text.strip(), "entry line must not be blank"


validate(line)
print(line)
