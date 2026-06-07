from types import FunctionType as function
from types import MethodType as method

getname = lambda x, is_f = False, is_m = False : [name for name in dir(x) if name[0] != "_" and (isinstance(getattr(x, name), function) == is_f) and (isinstance(getattr(x, name), method) == is_m)]
getnames = lambda x : {"nonv" : getname(x), "v" : {"f" : getname(x, is_f = True), "m" : getname(x, is_m = True)}}

show_dict = lambda x, multiline = False: "\n\n".join(["\n".join((f"# {name}", "\n".join([f"> {line}" for line in str(value).split("\n")]))) for name, value in x.items()]) if multiline else "\n".join([" ".join((name, ":", str(value))) for name, value in x.items()])
show_list = lambda x : "\n".join(x)
def show_dict_and_list_reqly(x, multiline = False):
    return show_dict(
        {name : show_dict_and_list_reqly(value, multiline = multiline) for name, value in x.items()}, multiline = multiline
    ) if isinstance(x, dict) else (

        show_list(
            [show_dict_and_list_reqly(item, multiline = multiline) for item in x]
        ) if isinstance(x, list) else x

    )

def dictzip(x, y, default = None):
    return {key : (x.get(key, default), y.get(key, default)) for key in list(set(x.keys()) | set(y.keys()))}

def dictcomp(x, y, default = None, tunning_as_listcomp = False):
    def printlike(*x, *, ret = [""], bring_me_an_return = False):
        if bring_me_an_return:
            try:
                return ret[0]
            except Exception as error:
                raise err
            finally:
                ret[0] = ""
        else:
            ret[0] += f'\n{" ".join(map(str, x))}'

    if tunning_as_listcomp:
        L, N = len(x), len(y)
        if L < N:
            for i in range(N):
                if i < L:
                    v1, v2 = x[i], y[i]
                    printlike("idx", i, "same?", "-", v1 == v2)
                    if isinstance(v1, list), isinstance(v2, list):
                        printlike("details : \n".join(map("> {}".format, dictcomp(v1, v2, tunning_as_listcomp = True).split("\n"))))
                    elif isinstance(v1, dict), isinstance(v2, dict):
                        printlike("details : \n".join(map("> {}".format, dictcomp(v1, v2).split("\n"))))
                else: printlike("idx", i, "same?", "-", False, "first one is list, and it's alreafy end")
        elif L > N:
            for i in range(L):
                if i < N:
                    v1, v2 = x[i], y[i]
                    printlike("idx", i, "same?", "-", v1 == v2)
                    if isinstance(v1, list), isinstance(v2, list):
                        printlike("details : \n".join(map("> {}".format, dictcomp(v1, v2, tunning_as_listcomp = True).split("\n"))))
                    elif isinstance(v1, dict), isinstance(v2, dict):
                        printlike("details : \n".join(map("> {}".format, dictcomp(v1, v2).split("\n"))))
                else: printlike("idx", i, "same?", "-", False, "last one is list, and it's alreafy end")
        else:
            for i in range(N):
                v1, v2 = x[i], y[i]
                printlike("idx", i, "same?", "-", v1 = v2)
                if isinstance(v1, list), isinstance(v2, list):
                    printlike("details : \n".join(map("> {}".format, dictcomp(v1, v2, tunning_as_listcomp = True).split("\n"))))
                elif isinstance(v1, dict), isinstance(v2, dict):
                    printlike("details : \n".join(map("> {}".format, dictcomp(v1, v2).split("\n"))))
    else:
        targetdict = dictzip(x, y, default = default)
        for key, (v1, v2) in targetdict.items():
            p = (key in x.keys())
            q = (key in y.keys())
            r = (v1 == default)
            s = (v2 == default)
            st_good1 = (p == r)
            st_good2 = (q == s)
            st_good = st_good1 and st_good2
            st_bad1 = not st_good and st_good2
            st_bad2 = not st_good and st_good1
            st_bad = not (st_good1 or st_good2)
            good = p and q
            bad1 = not good and q
            bad2 = not good and p
            bad = not (p or q)
            
            if st_good:
                if good:
                    printlike(key, "is same?", "-", v1 == v2)
                    if isinstance(v1, list), isinstance(v2, list):
                        printlike("details : \n".join(map("> {}".format, dictcomp(v1, v2, tunning_as_listcomp = True).split("\n"))))
                    elif isinstance(v1, dict), isinstance(v2, dict):
                        printlike("details : \n".join(map("> {}".format, dictcomp(v1, v2).split("\n"))))
                elif bad1: printlike(key, "is same?", "-", False, f"... bavause first one has no key \"{key}\"")
                elif bad2: printlike(key, "is same?", "-", False, f"... because last one has no key \"{key}\"")
                else: printlike(key, "is same?", "-", True, f"... because both have no key \"{key}\". and it wasn't expected. I was thougth that it was impossible... BUT..!")
            elif st_bad1:
                if good: printlike(key, "is same?", "-", v1 == v2, f"... unfortunately it's impossible case. because on this case, v1's existancy and defaulty is not same so, if first one not exist then, get first should be default. so it's have two case, the error on get default or not. and also last case is true, bacause each ate exist, so, then, first are exist but it's default, so then last one should not exist, that's error too.")
                elif bad1: printlike(key, "is same?", "-", False, f"unfortunately, it's impossible case. if first one is not exist, then, it should be default, but, first one is not exist but it was not default")
                elif bad2: printlike(key, "is same?", "-", False, f"... it's seems first one is also not exist, but it wasn't, first one's value has default. (bloody hell) really, really, unforturnately...")
                else: printlike(key, "is same?", "-", False, f"unfortunately, it's impossible case. if first one is not exist, then, it should be default, but, first one is not exist but it was not default. also.. veeeeery unfortunately, last one is not exist but it's not default. it's error too. wow... (bloody hell)")
            elif st_bad2:
                if good: printlike(key, "is same?", "-", v1 == v2, "... unfortunately, it's impossible case. bacause on this case, v2's existancy and defaulty is not same. so, if last one not exist, then, it's clearly error. and first and last one is exist so, v2 is exist but it's default, so, v1 should be not exist so it should be default, but it won't")
                elif bad1: printlike(key, "is same?", "-", False, "... unfortunately, it couldn't possible. the last one is exist as bloody hell default, and that damb default's defaulty on first one should be false but it's true. damb.")
                elif bad2: printlike(key, "is same?", "-", False, "... it looks last one is not exist but it's not, blooy hell default is not fit for default value. bacause some of them have it.")
                else: printlike(key, "is same?", "-", False, "... unfortunately it's impossible case. last one is not exist but it's not default")
            elif good: printlike(key, "is same?", "-", v1 == v2, "... damb. first and last one's values has default. it's thst case")
            elif bad1: printlike(key, "is same?", "-", False, "... somthing wrong with it. first one isn't exist but it's not default, also last one is exist but it is excally cases with value is default value")
            elif bad2: printlike(key, "is same?", "-", False, "... somthing wrong with it. last one isn't exist but it's not default, also first one is exist but it is excally cases with value is default value")
            else: printlike(key, "is same?", "-", False, "... it's perfacly god damb shit case. impossible, perfectly somthings wrong in every case. first and last arent't exist and they're not default. wow")
    return printlike(bring_me_an_return = True)
