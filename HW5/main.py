import matplotlib.pyplot as plt
from lg import *

def plot_N_loss():
    all_train_losses = []
    all_test_losses = []
    for i in range(1, 49):
        train_loss, test_loss = run_train_test(i)
        all_train_losses.append(train_loss)
        all_test_losses.append(test_loss)

    N = [i for i in range(1, 49)]
    plt.plot(N, all_train_losses, 'b', label='train')
    plt.plot(N, all_test_losses, 'r', label='test')
    plt.legend()
    plt.xlabel('N')
    plt.ylabel('MSE loss')
    plt.savefig('result.png')

def run_train_test(N):
    train_X, train_Y = read_train_csv('data/train.csv', N)
    model = Linear_Regression()
    model.train(train_X, train_Y)
    pred_train_Y = model.predict(train_X)
    train_loss = MSE(pred_train_Y, train_Y)

    test_X, test_Y = read_test_csv('data/test.csv', N)
    pred_test_Y = model.predict(test_X)
    test_loss = MSE(pred_test_Y, test_Y)
    print(train_loss, test_loss)    
    return train_loss, test_loss

if __name__ == '__main__' :
    N = 6
    run_train_test(N)
    plot_N_loss()

