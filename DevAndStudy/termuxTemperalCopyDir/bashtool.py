from functools import wraps as smart_deco_wraps
from os import remove as rm

def wither(opener = open, iter = False, asyncdef = False, asyncwith = False, awaitfunc = False):
    if iter and asyncdef and asyncwith and awaitfunc:
        @smart_deco_wrape(wither)
        def deco(func):
            @smart_deco_wraps(func)
            async def ret(*argv, **kargv):
                async with opener(*argv, **kargv) as fp:
                    yield from await func(fp, *argv, **kargv)
            return ret
    elif iter and asyncdef and awaitfunc:
        @smart_deco_wraps(wither)
        def deco(func):
            @smart_deco_wraps(func)
            async def ret(*argv, **kargv):
                with opener(*argv, **kargv) as fp:
                    yield from await func(fp, *argv, **kargv)
            return ret
    elif iter and asyncdef and asyncwith:
        @smart_deco_wraps(wither)
        def deco(func):
            @smart_deco_wraps(func)
            async def ret(*argv, **kargv):
                async with opener(*argv, **kargv) as fp:
                    yield from await func(fp, *argv, **kargv)
            return ret
    elif iter and asyncdef:
        @smart_deco_wraps(wither)
        def deco(func):
            @smart_deco_wraps(func)
            async def ret(*argv, **kargv):
                with opener(*argv, **kargv) as fp:
                    yield from func(fp, *argv, **kargv)
            return ret
    elif asyncdef and asyncwith and awaitfunc:
        @smart_deco_wraps(func)
        def deco(func):
            @smart_deco_wraps(func)
            async def ret(*argv, **kargv):
                async with opener(*argv, **kargv) as fp:
                    return await func(fp, *argv, **kargv)
            return ret
    elif asyncdef and awaitfunc:
        @smart_deco_wraps(func)
        def deco(func):
            @smart_deco_wraps(func)
            async def ret(*argv, **kargv):
                with opener(*argv, **kargv) as fp:
                    return await func(fp, *argv, **kargv)
            return ret
    elif asyncdef and asyncwith:
        @smart_deco_wraps(func)
        def deco(func):
            @smart_deco_wraps(func)
            async def ret(*argv, **kargv):
                async with opener(*argv, **kargv) as fp:
                    return func(fp, *argv, **kargv)
            return deco
    elif asyncdef:
        @smart_deco_wraps(func)
        def deco(func):
            @smart_deco_wraps(func)
            async def ret(*argv, **kargv):
                with opener(*argv, **kargv) as fp:
                    return func(fp, *argv, **kargv)
            return ret
    elif iter:
        @smart_deco_wraps(wither)
        def deco(func):
            @smart_deco_wraps(func)
            def ret(*argv, **kargv):
                with opener(*argv, **kargv) as fp:
                    yield from func(fp, *argv, **kargv)
            return ret
    else:
        @smart_deco_wraps(wither)
        def deco(func):
            @smart_deco_wraps(func)
            def ret(*argv, **kargv):
                with opener(*argv, **kargv) as fp:
                    return func(fp, *argv, **kargv)
            return ret
    return deco

@wither()
def txtdump(fp, filename, value, format = False):
    return fp.write(value.format(filename)) if format else fp.write(value)

@wither()
def txtload(fp, filename, return_list = None):
    if type(return_list) == list and len(return_list) == 1:
        return_list[0] = fp.read()
        return None
    else:
        return fp.read()

cmdpath = "/bin/{}".format

def cmdadd(name, src):
    return txtdump(
        cmdpath(name),
        f"""\
        #!/bin/sh

        chmod u+x {{}}

        {src}\
        """
    )

def cmdpop(name):
    return rm(cmdpath(name))
