'''this is an fakes auth for using you..'''

__version__ : int = 1.1


__count__: int = 66
__auths__: list = ['zcjtvmevwxkmbemxwtquawrtacdptofe', 'joayzasxklhbaewxvwqoekpflmqebrvd', 'pqytjkzeepdhwsqmsjpkalgsqbdvtifl', 'svnsxthxnsgvpxrnaslreocepusajiup', 'qoymiijfhvguzzykoqtzdluaveorzsao', 'qoymiijfhvguzzykoqtzdluaveorzsao', 'mqdzdmzszqepxdinuepgnwryochljnmq', 'esxnvvvdgwypoeqhizteunhangajmsgg', 'jtfmnyquckeqqjadcwgjuhxohnatzpjq', 'gjtbussxotfqzfobxrfilyfmqcmurrae', 'wdqpwzsaerpdxbbxytohcayvsngcrbcy', 'yjlwlfrxskfvdfahfppgnnnofisnpeej', 'yjlwlfrxskfvdfahfppgnnnofisnpeej', 'xcnojhdvhoedwjodmwrnnirmsnqlvlyl', 'slpzydyitaergvuykelhapwpsjpebknf', 'zhvcqntwfygxlibbixwacqfqucenuxke', 'giimyvytyjjtutgbmczcethgkgvjviof', 'thidcsqyaxskdrcqegmkbqdttscdefwa', 'thidcsqyaxskdrcqegmkbqdttscdefwa', 'cqcedifaqbxmwdwqodfdetgeghwpaytb', 'wsdwlukbqlpbjtzuqelunsmicumrrlqq', 'xoqlbaoztkbbiqthryyasjpysvjydzyn', 'wcwfqxoltnqkederhrppaiwfmmyvcqkb', 'ijhmxuugmjgfldzvqfpnlotdrwnmqzai', 'pamtvelhvjvqqptphommbdrhjnvxlujg', 'bhhovjdbxumiynqhnvqpwmlrrqcgmcvg', 'nniefkufdlzwqxhkjkztjauvhwufcmvv', 'pxbcncjnrzjdcdzvhuapvfbbkuwmhmry', 'yemppaprgfqgcajcrrrssgulwrbhmfpp', 'wlhcmydcgzcgdutyhjpbecpjhlltkeed', 'dkzsmjxclfjvzoovgehtnvtalwdhvzrs', 'dkzsmjxclfjvzoovgehtnvtalwdhvzrs', 'dkzsmjxclfjvzoovgehtnvtalwdhvzrs', 'uiwbavbvkvzboygdakklmiutscxhqofs', 'yohlzhoapxzdfgudjgmrhljzuawuxotu', 'jzojqdikckdcppnrqarosuvupwtpnoki', 'bbfbeildwcwwjzhzvsokephgrnuedztt', 'yylnjelugekhhwrelpxoficlhhgjemuv', 'tgteavgzqczhlqbbcgipsrucnnyulufq', 'lzxcbxwgkemvzdlzqxhmqutgddpiiugn', 'bmwlggphczvgyelxryzpxcjerlwqoraq', 'mlzsiyigvdkltitjghvltyaulgreheeb', 'qhiklgnptauuytsuqxzuabisbglihhax', 'eztoudzhjzehgveeggsbrfotaharcqzp', 'yemosaywuggxeveogbcyavxodavhplgj', 'amphibcrfwvpvukquxhbphhcoaqzblvk', 'taoavxihfjhddsqjgxosenevnnmlowaa', 'xcthqwiblfckicauhkqdazhuvecneaea', 'qsziqsnvtzvvirkmntjupitoasuhyydi', 'mifuftcdnhikwqmumybqdcbhgybljamu', 'zcftcgtxyxfuezepyidvsoqojbmvuafj', 'kpblvljxwhakckokblvmadfuesreumxl', 'ewyzhkaruwpzmpzywidmbjfirasdccus', 'gjlaemzpjxzndigccqxyuhxfjjygwrse', 'xdofjzeblvxqaychprauwfibimgrjhve', 'yqntukimwropqcixujecdavuzybpoarn', 'ehmyphyziifxzpzkrndvtocwcfkejhxc', 'qcsobtmnjlvnfzsdakudjfcgqjqtuqby', 'qcsobtmnjlvnfzsdakudjfcgqjqtuqby', 'zoxpvodxjffmbtxgwxzvtilostdwxfan', 'ovcxtrbcdsmbalrziurglqmrnqswasrg', 'jxaxjjmnvmsimiwabwbjtbhhvkjjtcoz', 'xuximhcrbrwxwtpkoefakesyhiqtniag', 'xuximhcrbrwxwtpkoefakesyhiqtniag', 'ekvaxkzbyuemqxjicplibjhmauvwneab', 'bpcpsbrrvfyttshomvgkhuvkkgqqnrlo']

def rnd() -> str:
    '''return a random auth
    !NOTE: The possibility of problems in auths is certain'''
    from random import choice
    return choice(__auths__).lower()
