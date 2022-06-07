## NORMA USD TAB 
command_Norma_usdt_closeBotton = ''
command_Norma_usdt_connectBotton = ''
command_Norma_usdt_killBotton = 'tmux attach-session -t TEST -d'
command_Norma_usdt_startBotton = 'bash start_norma_arbitrage.sh norma.json'
command_Norma_usdt_stopBotton = 'bash stop_norma_arbitrage.sh norma.json'

ssh_Norma_usdt_host = '89.58.33.148'
ssh_Norma_usdt_user = 'root'
ssh_Norma_usdt_pwd = '5DUYMDBg55ahFGH'

## NORMA BTC TAB 
command_Norma_btc_closeBotton = ''
command_Norma_btc_connectBotton = ''
command_Norma_btc_killBotton = ''
command_Norma_btc_startBotton = 'bash start_norma_arbitrage.sh norma.json'
command_Norma_btc_stopBotton = 'bash stop_norma_arbitrage.sh norma.json'

ssh_Norma_btc_host = '89.58.33.148'
ssh_Norma_btc_user = 'root'
ssh_Norma_btc_pwd = '5DUYMDBg55ahFGH'

## KUOTER TAB 
command_Kuoter_closeBotton = ''
command_Kuoter_connectBotton = ''
command_Kuoter_killBotton = ''
command_Kuoter_startBotton = 'pm2 start k01 k02 k03 k04 k05'
command_Kuoter_stopBotton = 'pm2 stop k01 k02 k03 k04 k05'

ssh_Kuoter_host = '202.61.199.210'
ssh_Kuoter_user = 'root'
ssh_Kuoter_pwd = 'yQVzZc2EeA6cG9R'

## LETTORE TAB 
command_Lettore_closeBotton = ''
command_Lettore_connectBotton = ''
command_Lettore_startBotton = 'pm2 start getbooks01 getbooks02 getbooks03 getbooks04 getbooks05'
command_Lettore_stopBotton = 'pm2 stop getbooks01 getbooks02 getbooks03 getbooks04 getbooks05'

ssh_Lettore_host = '93.104.211.241'
ssh_Lettore_user = 'root'
ssh_Lettore_pwd = 'KMsB87du'

## GLMR TAB 
command_Glmr_closeBotton = ''
command_Glmr_connectBotton = ''
command_Glmr_startBotton = 'python main.py binanceGLMRUSDTon.json'
command_Glmr_stopBotton = "serial.write(b'\x03')"

ssh_Glmr_host = '89.58.33.148'
ssh_Glmr_user = 'root'
ssh_Glmr_pwd = '5DUYMDBg55ahFGH'
