# This program demonstrate how to extract function's signature.

def clip(text: str, max_len:'int > 0'=80) -> str:
    # Annotations will be stored in __annotations__, and won't change anything of this function
    # But could use this mechanism to provide more information to the editor for auto-completion/static type checking, etc..
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)
    return text[:end].rstrip()

if __name__ == "__main__":
    from inspect import signature
    sig = signature(clip)
    print(sig, str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

    