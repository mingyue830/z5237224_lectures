import os
import yfexample_2
import toolkit_config as cfg

def qan_prc_to_csv(year):
    tic = 'QAN.AX'
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    df = yfexample_2.yf_prc_to_csv(
        tic = tic,
        pth = pth,
        start = start,
        end = end,
    )

if __name__ == '__main__':
    year = 2020
    qan_prc_to_csv(year)
