from optparse import OptionParser
def parseOpt(modeArray):
    parser = OptionParser()
    parser.add_option("-v", action="count", dest="verbose", default=0, help="verbose count")
    parser.add_option("-q", action="store_true", dest="quiet",default="true", help="quiet mode")
    parser.add_option("-p","--parrot", action="store_true", dest="parrotMode", default="false", help="parrot mode")
    parser.add_option("-r","--rage", action="store_true", dest="rageParrotMode", default="false", help="rage parrot Mode")

    (options, args) = parser.parse_args()

    modeArray[0] = options.verbose
    modeArray[1] = options.parrotMode
    modeArray[2] = options.rageParrotMode
    modeArray[3] = options.quiet


