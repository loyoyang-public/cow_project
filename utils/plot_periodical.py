import numpy as np
from matplotlib import pyplot as plt

# plot TP/FP/FN cases along periods
# label and score should be n*(dim of data), n should correspond to len(periods)


def periodical_confusion_matrix(label,score,periods):
    fp = []
    tp = []
    fn = []
    
    width = 0.5
    
    for i in periods:
        
        # get best cut-off
        fp_,tp_,thresh = roc_curve(label[i], score[i])
        j_scores = tp_-fp_
        j_ordered = sorted(zip(j_scores,thresh))
        threshold = j_ordered[-1][1]
        
        pred = [0 if x < threshold else 1 for x in score[i]]
        
        result = confusion_matrix(label[i], pred)
        fp.append(result[0,1])
        tp.append(result[1,1])
        fn.append(result[1,0])
         
    # plot FP downwards
    fp = [x*(-1) for x in fp]
    
    fp = np.array(fp)
    tp = np.array(tp)

    plt.figure()
    
    plt.ylim([-12000,20000])
    plt.yticks(np.arange(-12000,20000,2500))
    
    p1 = plt.bar(periods,tp,width,color = 'royalblue')
    p2 = plt.bar(periods,fp,width,color='darkorange')
    p3 = plt.bar(periods,fn,width,bottom=tp,alpha=0.6,color='c')
    x_ticks = np.arange(0,120,10)
    
    plt.xlabel('Periods', fontsize=18, color = 'royalblue')
    plt.ylabel('#cases', fontsize=18, color = 'royalblue')
    plt.xticks(x_ticks[::-1])
    axes = plt.gca()
    axes.set_xlim([120,0])
    plt.legend((p1[0],p2[0],p3[0]),('TP','FP','FN'),loc=3)
    plt.title('TP vs. FP along periods',fontsize = 20)
    plt.rcParams['figure.figsize'] = [15, 10]
    plt.grid(True, color = 'lightgray')

    plt.show()
