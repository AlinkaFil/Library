class UserError(AttributeError):
    pass


class BookError(AttributeError):
    pass


class BookIssuedError(AttributeError):
    pass

class IssueLimitError(AttributeError):
    pass


class NoPublishedBooksError(AttributeError):
    pass
