import backtrader

cerebro = backtrader.Cerebro()

cerebro.broker.set_cash(1000000)
print('Starting Portfolio value: %.2f' % cerebro.broker.get_value())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.get_value())