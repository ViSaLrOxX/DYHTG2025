dat = yf.Ticker("MSFT")

dat = yf.Ticker("MSFT")
dat.info
dat.calendar
dat.analyst_price_targets
dat.quarterly_income_stmt
dat.history(period='1mo')
dat.option_chain(dat.options[0]).calls

tickers = yf.Tickers('MSFT AAPL GOOG')
tickers.tickers['MSFT'].info
yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo')

spy = yf.Ticker('SPY').funds_data
spy.description
spy.top_holdings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Set up plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# =============================================================================
# MOCK DATA CLASSES (From previous implementation)
# =============================================================================

class MockTicker:
    def __init__(self, symbol):
        self.symbol = symbol
        
    @property
    def info(self):
        base_info = {
            'MSFT': {
                'currentPrice': 378.45, 'marketCap': 2810000000000, 'sector': 'Technology',
                'forwardPE': 28.45, 'dividendYield': 0.0079, 'profitMargins': 0.35
            },
            'AAPL': {
                'currentPrice': 185.25, 'marketCap': 2900000000000, 'sector': 'Technology', 
                'forwardPE': 26.80, 'dividendYield': 0.0052, 'profitMargins': 0.28
            },
            'GOOG': {
                'currentPrice': 135.67, 'marketCap': 1700000000000, 'sector': 'Communication Services',
                'forwardPE': 22.15, 'dividendYield': 0.0, 'profitMargins': 0.24
            }
        }
        info = base_info.get(self.symbol, base_info['MSFT'])
        info.update({
            'symbol': self.symbol,
            'longName': f'{self.symbol} Corporation',
            'shortName': self.symbol,
            'exchange': 'NMS',
            'currency': 'USD',
            'targetHighPrice': info['currentPrice'] * 1.15,
            'targetLowPrice': info['currentPrice'] * 0.85,
            'targetMeanPrice': info['currentPrice'] * 1.02,
            'recommendationMean': 1.8,
            'recommendationKey': 'buy',
            'numberOfAnalystOpinions': 42,
            'totalRevenue': 218310000000,
            'revenuePerShare': 73.12,
            'trailingPE': info['forwardPE'] * 1.1,
            'volume': 28500000,
            'averageVolume': 27500000,
            'fiftyTwoWeekHigh': info['currentPrice'] * 1.05,
            'fiftyTwoWeekLow': info['currentPrice'] * 0.75,
            'dividendRate': 3.00 if self.symbol != 'GOOG' else 0.0,
            'payoutRatio': 0.268,
            'beta': 0.89,
            'website': f'https://www.{self.symbol.lower()}.com',
            'industry': 'Software—Infrastructure' if self.symbol == 'MSFT' else 'Consumer Electronics',
            'fullTimeEmployees': 221000,
            'country': 'United States'
        })
        return info
    
    @property
    def calendar(self):
        return {
            'earningsDate': [datetime(2024, 1, 25), datetime(2024, 1, 26)],
            'exDividendDate': datetime(2024, 2, 15),
            'dividendDate': datetime(2024, 3, 14)
        }
    
    @property
    def analyst_price_targets(self):
        return pd.DataFrame({
            'symbol': [self.symbol] * 5,
            'currentPrice': [self.info['currentPrice']] * 5,
            'targetPrice': [
                self.info['currentPrice'] * 1.15,
                self.info['currentPrice'] * 1.10,
                self.info['currentPrice'] * 1.05,
                self.info['currentPrice'] * 0.98,
                self.info['currentPrice'] * 0.95
            ],
            'provider': ['Morgan Stanley', 'Goldman Sachs', 'JP Morgan', 'Barclays', 'Wells Fargo'],
            'rating': ['Overweight', 'Buy', 'Neutral', 'Equal-Weight', 'Hold'],
            'publishedDate': [
                datetime(2024, 1, 10), datetime(2024, 1, 8), datetime(2024, 1, 5),
                datetime(2024, 1, 3), datetime(2023, 12, 28)
            ]
        })
    
    @property
    def quarterly_income_stmt(self):
        dates = [datetime(2023, 9, 30), datetime(2023, 6, 30), datetime(2023, 3, 31), datetime(2022, 12, 31)]
        base_revenue = 50000e6 if self.symbol == 'MSFT' else 80000e6 if self.symbol == 'AAPL' else 60000e6
        return pd.DataFrame({
            'Total Revenue': [base_revenue * 1.1, base_revenue * 1.05, base_revenue, base_revenue * 0.95],
            'Gross Profit': [base_revenue * 0.65, base_revenue * 0.63, base_revenue * 0.62, base_revenue * 0.60],
            'Operating Income': [base_revenue * 0.35, base_revenue * 0.33, base_revenue * 0.32, base_revenue * 0.30],
            'Net Income': [base_revenue * 0.25, base_revenue * 0.23, base_revenue * 0.22, base_revenue * 0.20],
            'EPS': [2.99, 2.69, 2.45, 2.20]
        }, index=dates)
    
    def history(self, period='1mo'):
        end_date = datetime.now()
        days = 30 if period == '1mo' else 90 if period == '3mo' else 365
        start_date = end_date - timedelta(days=days)
        dates = pd.date_range(start=start_date, end=end_date, freq='D')
        
        np.random.seed(hash(self.symbol) % 1000)
        base_price = self.info['currentPrice']
        returns = np.random.normal(0.001, 0.02, len(dates))
        prices = base_price * (1 + returns).cumprod()
        
        return pd.DataFrame({
            'Open': prices * (1 + np.random.normal(0, 0.005, len(dates))),
            'High': prices * (1 + np.abs(np.random.normal(0.01, 0.008, len(dates)))),
            'Low': prices * (1 - np.abs(np.random.normal(0.008, 0.006, len(dates)))),
            'Close': prices,
            'Volume': np.random.randint(20000000, 35000000, len(dates)),
            'Dividends': [0] * len(dates),
            'Stock Splits': [0] * len(dates)
        }, index=dates)
    
    @property
    def options(self):
        return ['2024-01-19', '2024-02-16', '2024-03-15', '2024-06-21', '2024-09-20']
    
    def option_chain(self, date):
        class MockOptionChain:
            def __init__(self, symbol, current_price):
                strikes = np.arange(current_price * 0.9, current_price * 1.1, 5)
                self.calls = pd.DataFrame({
                    'strike': strikes,
                    'lastPrice': (current_price * 1.1 - strikes) * 0.8,
                    'impliedVolatility': np.random.uniform(0.2, 0.3, len(strikes)),
                    'volume': np.random.randint(100, 2000, len(strikes)),
                    'openInterest': np.random.randint(1000, 10000, len(strikes))
                })
                self.puts = pd.DataFrame({
                    'strike': strikes,
                    'lastPrice': (strikes - current_price * 0.9) * 0.8,
                    'impliedVolatility': np.random.uniform(0.25, 0.35, len(strikes)),
                    'volume': np.random.randint(100, 2000, len(strikes)),
                    'openInterest': np.random.randint(1000, 10000, len(strikes))
                })
        return MockOptionChain(self.symbol, self.info['currentPrice'])

class MockTickers:
    def __init__(self, symbols):
        self.symbol_list = symbols.split()
        self.tickers = {symbol: MockTicker(symbol) for symbol in self.symbol_list}

def mock_download(symbols, period='1mo'):
    if isinstance(symbols, str):
        symbols = [symbols]
    
    end_date = datetime.now()
    days = 30 if period == '1mo' else 90 if period == '3mo' else 365
    start_date = end_date - timedelta(days=days)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    data = {}
    for symbol in symbols:
        np.random.seed(hash(symbol) % 1000)
        base_price = {'MSFT': 375, 'AAPL': 185, 'GOOG': 135}[symbol]
        returns = np.random.normal(0.001, 0.018, len(dates))
        prices = base_price * (1 + returns).cumprod()
        
        df = pd.DataFrame({
            'Open': prices * (1 + np.random.normal(0, 0.004, len(dates))),
            'High': prices * (1 + np.abs(np.random.normal(0.009, 0.007, len(dates)))),
            'Low': prices * (1 - np.abs(np.random.normal(0.007, 0.005, len(dates)))),
            'Close': prices,
            'Volume': np.random.randint(15000000, 40000000, len(dates)),
            'Adj Close': prices
        }, index=dates)
        
        columns = pd.MultiIndex.from_product([[symbol], df.columns])
        df.columns = columns
        data[symbol] = df
    
    return pd.concat(data.values(), axis=1)

# =============================================================================
# ANALYSIS IMPLEMENTATION
# =============================================================================

class FinancialAnalyzer:
    def __init__(self):
        self.stocks = {}
    
    def add_stock(self, symbol):
        """Add a stock to analyze"""
        self.stocks[symbol] = MockTicker(symbol)
        return self.stocks[symbol]
    
    def basic_company_analysis(self, symbol):
        """Comprehensive company analysis"""
        stock = self.add_stock(symbol)
        info = stock.info
        
        print(f"\n{'='*60}")
        print(f"📊 COMPREHENSIVE ANALYSIS: {symbol}")
        print(f"{'='*60}")
        
        # Basic Info
        print(f"\n🏢 COMPANY INFORMATION:")
        print(f"   Name: {info['longName']}")
        print(f"   Sector: {info['sector']}")
        print(f"   Industry: {info['industry']}")
        print(f"   Market Cap: ${info['marketCap']/1e9:.1f}B")
        print(f"   Employees: {info['fullTimeEmployees']:,}")
        
        # Financial Metrics
        print(f"\n💰 FINANCIAL METRICS:")
        print(f"   Current Price: ${info['currentPrice']:.2f}")
        print(f"   P/E Ratio: {info['forwardPE']:.1f}")
        print(f"   P/E (Trailing): {info['trailingPE']:.1f}")
        print(f"   Profit Margin: {info['profitMargins']*100:.1f}%")
        print(f"   Dividend Yield: {info['dividendYield']*100:.2f}%" if info['dividendYield'] else "   Dividend Yield: None")
        print(f"   Beta: {info['beta']:.2f}")
        
        # Analyst Ratings
        print(f"\n🎯 ANALYST OPINIONS:")
        targets = stock.analyst_price_targets
        print(f"   Mean Target: ${info['targetMeanPrice']:.2f}")
        print(f"   Upside: {(info['targetMeanPrice']/info['currentPrice']-1)*100:+.1f}%")
        print(f"   Recommendation: {info['recommendationKey'].title()}")
        print(f"   Analysts Covering: {info['numberOfAnalystOpinions']}")
        
        return info
    
    def technical_analysis(self, symbol, period='3mo'):
        """Technical analysis with indicators"""
        stock = self.add_stock(symbol)
        hist = stock.history(period=period)
        
        # Calculate indicators
        hist['SMA_20'] = hist['Close'].rolling(window=20).mean()
        hist['SMA_50'] = hist['Close'].rolling(window=50).mean()
        hist['RSI'] = self.calculate_rsi(hist['Close'])
        
        current_price = hist['Close'].iloc[-1]
        sma_20 = hist['SMA_20'].iloc[-1]
        rsi = hist['RSI'].iloc[-1]
        
        print(f"\n📈 TECHNICAL ANALYSIS ({period}):")
        print(f"   Current Price: ${current_price:.2f}")
        print(f"   20-Day SMA: ${sma_20:.2f}")
        print(f"   RSI: {rsi:.1f}")
        
        # Generate signals
        trend = "BULLISH 📈" if current_price > sma_20 else "BEARISH 📉"
        if rsi > 70:
            rsi_signal = "OVERSOLD 🚨"
        elif rsi < 30:
            rsi_signal = "OVERBOUGHT 🚨"
        else:
            rsi_signal = "NEUTRAL ⚖️"
        
        print(f"   Trend: {trend}")
        print(f"   RSI Signal: {rsi_signal}")
        
        return hist
    
    def calculate_rsi(self, prices, window=14):
        """Calculate Relative Strength Index"""
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))
    
    def financial_statement_analysis(self, symbol):
        """Analyze financial statements"""
        stock = self.add_stock(symbol)
        income_stmt = stock.quarterly_income_stmt
        
        print(f"\n📋 FINANCIAL STATEMENT ANALYSIS:")
        print(f"   Revenue Trend: {self._calculate_growth(income_stmt['Total Revenue']):+.1f}%")
        print(f"   Net Income Trend: {self._calculate_growth(income_stmt['Net Income']):+.1f}%")
        print(f"   EPS Trend: {self._calculate_growth(income_stmt['EPS']):+.1f}%")
        
        return income_stmt
    
    def _calculate_growth(self, series):
        """Calculate percentage growth from first to last period"""
        if len(series) < 2:
            return 0
        return ((series.iloc[0] / series.iloc[-1]) - 1) * 100
    
    def options_analysis(self, symbol):
        """Analyze options chain"""
        stock = self.add_stock(symbol)
        options_data = stock.option_chain(stock.options[0])
        
        print(f"\n🎪 OPTIONS ANALYSIS:")
        print(f"   Next Expiration: {stock.options[0]}")
        
        calls = options_data.calls
        puts = options_data.puts
        
        total_call_oi = calls['openInterest'].sum()
        total_put_oi = puts['openInterest'].sum()
        put_call_ratio = total_put_oi / total_call_oi
        
        print(f"   Total Call OI: {total_call_oi:,}")
        print(f"   Total Put OI: {total_put_oi:,}")
        print(f"   Put/Call Ratio: {put_call_ratio:.2f}")
        
        sentiment = "Bearish" if put_call_ratio > 1.0 else "Bullish"
        print(f"   Options Sentiment: {sentiment}")
        
        return options_data

class PortfolioManager:
    def __init__(self, symbols):
        self.symbols = symbols
        self.tickers = MockTickers(' '.join(symbols))
        self.analyzer = FinancialAnalyzer()
    
    def portfolio_overview(self):
        """Generate portfolio overview"""
        print(f"\n{'='*60}")
        print(f"💼 PORTFOLIO OVERVIEW")
        print(f"{'='*60}")
        
        portfolio_data = []
        
        for symbol in self.symbols:
            stock = self.tickers.tickers[symbol]
            info = stock.info
            hist = stock.history('1mo')
            
            current_price = info['currentPrice']
            price_change = ((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100
            
            portfolio_data.append({
                'Symbol': symbol,
                'Price': f"${current_price:.2f}",
                'Change %': f"{price_change:+.2f}%",
                'Market Cap': f"${info['marketCap']/1e9:.0f}B",
                'P/E': f"{info['forwardPE']:.1f}",
                'Sector': info['sector'],
                'Div Yield': f"{info['dividendYield']*100:.2f}%" if info['dividendYield'] else "None"
            })
        
        portfolio_df = pd.DataFrame(portfolio_data)
        print(portfolio_df.to_string(index=False))
        
        return portfolio_df
    
    def correlation_analysis(self, period='3mo'):
        """Analyze correlation between stocks"""
        print(f"\n🔗 PORTFOLIO CORRELATION ANALYSIS:")
        
        # Get price data for all symbols
        close_prices = []
        for symbol in self.symbols:
            hist = self.tickers.tickers[symbol].history(period)
            close_prices.append(hist['Close'].rename(symbol))
        
        correlation_df = pd.concat(close_prices, axis=1).corr()
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_df, annot=True, cmap='coolwarm', center=0,
                   square=True, fmt='.2f', cbar_kws={'shrink': 0.8})
        plt.title('Stock Correlation Matrix')
        plt.tight_layout()
        plt.show()
        
        print(correlation_df)
        return correlation_df

# =============================================================================
# VISUALIZATION FUNCTIONS
# =============================================================================

def plot_price_comparison(symbols, period='3mo'):
    """Plot price comparison for multiple stocks"""
    plt.figure(figsize=(12, 8))
    
    for symbol in symbols:
        stock = MockTicker(symbol)
        hist = stock.history(period)
        # Normalize prices to percentage change
        normalized_prices = (hist['Close'] / hist['Close'].iloc[0] - 1) * 100
        plt.plot(normalized_prices.index, normalized_prices.values, label=symbol, linewidth=2)
    
    plt.title(f'Stock Performance Comparison ({period})')
    plt.ylabel('Price Change (%)')
    plt.xlabel('Date')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_technical_indicators(symbol, period='3mo'):
    """Plot technical indicators for a stock"""
    stock = MockTicker(symbol)
    hist = stock.history(period)
    
    # Calculate indicators
    hist['SMA_20'] = hist['Close'].rolling(window=20).mean()
    hist['SMA_50'] = hist['Close'].rolling(window=50).mean()
    hist['RSI'] = FinancialAnalyzer().calculate_rsi(hist['Close'])
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Price chart
    ax1.plot(hist.index, hist['Close'], label='Close Price', linewidth=2, color='blue')
    ax1.plot(hist.index, hist['SMA_20'], label='20-Day SMA', alpha=0.7, color='orange')
    ax1.plot(hist.index, hist['SMA_50'], label='50-Day SMA', alpha=0.7, color='red')
    ax1.set_title(f'{symbol} - Price and Moving Averages')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # RSI chart
    ax2.plot(hist.index, hist['RSI'], label='RSI', color='purple', linewidth=2)
    ax2.axhline(70, linestyle='--', color='red', alpha=0.7, label='Overbought (70)')
    ax2.axhline(30, linestyle='--', color='green', alpha=0.7, label='Oversold (30)')
    ax2.axhline(50, linestyle='--', color='gray', alpha=0.5, label='Neutral (50)')
    ax2.set_title('Relative Strength Index (RSI)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 100)
    
    plt.tight_layout()
    plt.show()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main execution function"""
    print("🚀 FINANCIAL DATA ANALYSIS PLATFORM")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = FinancialAnalyzer()
    portfolio_symbols = ['MSFT', 'AAPL', 'GOOG']
    
    # Individual stock analysis
    for symbol in portfolio_symbols:
        # Comprehensive analysis
        analyzer.basic_company_analysis(symbol)
        analyzer.technical_analysis(symbol)
        analyzer.financial_statement_analysis(symbol)
        analyzer.options_analysis(symbol)
    
    # Portfolio analysis
    portfolio = PortfolioManager(portfolio_symbols)
    portfolio.portfolio_overview()
    
    # Visualizations
    print(f"\n📊 GENERATING VISUALIZATIONS...")
    
    # Price comparison chart
    plot_price_comparison(portfolio_symbols, '3mo')
    
    # Technical analysis for MSFT
    plot_technical_indicators('MSFT', '3mo')
    
    # Correlation analysis
    portfolio.correlation_analysis('3mo')
    
    # Additional insights
    print(f"\n💡 KEY INSIGHTS:")
    print("1. MSFT shows strong fundamentals with good dividend yield")
    print("2. AAPL has largest market cap but lower growth in our mock data")
    print("3. GOOG has no dividend but lower P/E ratio")
    print("4. All stocks are positively correlated as expected in tech sector")
    print("5. Options data suggests market sentiment for each stock")

if __name__ == "__main__":
    main()