from .util import run_command


#  def test_allmusic():
#      run_command(["bnm", "am"], retcode=0)

#  def test_metacritic():
#      run_command(['bnm', 'mc'], retcode=0)


def test_wfmu():
    run_command(["bnm", "wfmu"], retcode=0)


def test_kalx():
    run_command(["bnm", "kalx"], retcode=0)


def test_pitchfork():
    run_command(["bnm", "p4k"], retcode=0)


def test_stranded():
    run_command(["bnm", "sd"], retcode=0)


def test_boomkat():
    run_command(["bnm", "bk"], retcode=0)


def test_resident_advisor():
    run_command(["bnm", "ra"], retcode=0)


def test_forced_exposure():
    run_command(["bnm", "fe"], retcode=0)


def test_midheaven():
    run_command(["bnm", "mh"], retcode=0)
