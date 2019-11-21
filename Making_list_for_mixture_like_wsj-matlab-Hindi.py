import os, random
import pandas as pd
import decimal


#Making list for tr as used to make mixture like wsj
row_list = []
for x in range(500):
    #wham_noise = random.choice(os.listdir("/media/reverie-pc/speech/asr/kaldi/egs/Neural-mask-estimation/wham_noise/tr/"))
    spkr1 = random.choice(os.listdir("/media/reverie-pc/speech/asr/kaldi/egs/Conv-TasNet/egs/wsj0/wsj0-hin/tr/"))
    spkr2 = random.choice(os.listdir("/media/reverie-pc/speech/asr/kaldi/egs/Conv-TasNet/egs/wsj0/wsj0-hin/tr/"))
    #data = [wham_noise,'wsj0/tr/'+spkr1,'wsj0/tr/'+spkr2]
    snr_1 = float(decimal.Decimal(random.randrange(1, 250))/100)
    snr_2 = -snr_1
    data = ['wsj0-hin/tr/'+spkr1, snr_1 ,'wsj0-hin/tr/'+spkr2, snr_2]
    row_list.append(data)
df = pd.DataFrame(row_list)    
#df = pd.read_csv(pd.compat.StringIO(row_list), header=None)
#df = pd.read_csv(row_list, header=None)
#df.columns = ['output_filename', 's1_path', 's2_path']
df.to_csv('/media/reverie-pc/speech/asr/kaldi/egs/Conv-TasNet/egs/wsj0/create-speaker-mixtures/mixhin_2_spk_tr.txt',index=False,sep=' ',header=False) 
#df_f = df.apppend()    


#Making list for cv as used to make mixture like wsj
row_list = []
for x in range(100):
    #wham_noise = random.choice(os.listdir("/media/reverie-pc/speech/asr/kaldi/egs/Neural-mask-estimation/wham_noise/cv/"))
    spkr1 = random.choice(os.listdir("/media/reverie-pc/speech/asr/kaldi/egs/Conv-TasNet/egs/wsj0/wsj0-hin/cv/"))
    spkr2 = random.choice(os.listdir("/media/reverie-pc/speech/asr/kaldi/egs/Conv-TasNet/egs/wsj0/wsj0-hin/cv/"))
    #data = [wham_noise,'wsj0/tr/'+spkr1,'wsj0/tr/'+spkr2]
    snr_1 = float(decimal.Decimal(random.randrange(1, 250))/100)
    snr_2 = -snr_1
    data = ['wsj0-hin/cv/'+spkr1, snr_1 ,'wsj0-hin/cv/'+spkr2, snr_2]
    row_list.append(data)
df = pd.DataFrame(row_list)    
#df = pd.read_csv(pd.compat.StringIO(row_list), header=None)
#df = pd.read_csv(row_list, header=None)
#df.columns = ['output_filename', 's1_path', 's2_path']
df.to_csv('/media/reverie-pc/speech/asr/kaldi/egs/Conv-TasNet/egs/wsj0/create-speaker-mixtures/mixhin_2_spk_cv.txt',index=False,sep=' ',header=False) 
#df_f = df.apppend()    



#Making list for tt as used to make mixture like wsj
row_list = []
for x in range(100):
    #wham_noise = random.choice(os.listdir("/media/reverie-pc/speech/asr/kaldi/egs/Neural-mask-estimation/wham_noise/tt/"))
    spkr1 = random.choice(os.listdir("/media/reverie-pc/speech/asr/kaldi/egs/Conv-TasNet/egs/wsj0/wsj0-hin/tt/"))
    spkr2 = random.choice(os.listdir("/media/reverie-pc/speech/asr/kaldi/egs/Conv-TasNet/egs/wsj0/wsj0-hin/tt/"))
    #data = [wham_noise,'wsj0/tr/'+spkr1,'wsj0/tr/'+spkr2]
    snr_1 = float(decimal.Decimal(random.randrange(1, 250))/100)
    snr_2 = -snr_1
    data = ['wsj0-hin/tt/'+spkr1, snr_1 ,'wsj0-hin/tt/'+spkr2, snr_2]
    row_list.append(data)
df = pd.DataFrame(row_list)    
#df = pd.read_csv(pd.compat.StringIO(row_list), header=None)
#df = pd.read_csv(row_list, header=None)
#df.columns = ['output_filename', 's1_path', 's2_path']
df.to_csv('/media/reverie-pc/speech/asr/kaldi/egs/Conv-TasNet/egs/wsj0/create-speaker-mixtures/mixhin_2_spk_tt.txt',index=False,sep=' ',header=False) 
#df_f = df.apppend()     
