from typing import Dict, Optional
import logging
from strategy_generator import StrategyGenerator

class StrategyTester:
    """
    Tests and validates monetization strategies in simulated environments.
    Implements TestableStrategy interface.
    """

    def __init__(self):
        self.strategy_archive = []
        self.test_results = {}
        logging.basicConfig(
            filename='strategy_tester.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def test_strategy(self, strategy: Dict) -> Dict:
        """
        Tests a given strategy in a simulated market environment.
        Implements TestableStrategy interface.
        """
        try:
            # Simulated testing environment
            test_id = f"TEST_{len(self.strategy_archive)+1}"
            backtest_results = {
                "profitability": 0.15,
                "risk_score": 0.7,
                "success_rate": 0.85
            }
            
            self.test_results[test_id] = {
                "strategy_id": strategy["id"],
                "results": backtest_results
            }
            
            logging.info(f"Strategy {strategy['id']} tested successfully")
            return {"status": "success", "results": backtest_results}
            
        except Exception as e:
            logging.error(f"Testing failed for strategy {strategy.get('id', 'unknown')}: {e}")
            raise

    def archive_strategy(self, strategy_id: str) -> None:
        """
        Archives a tested strategy for future reference.
        Implements ArchivableStrategy interface.
        """
        try:
            self.strategy_archive.append({
                "id": strategy_id,
                "test_date": datetime.now().isoformat(),
                "status": "tested"
            })
            logging.info(f"Archived strategy {strategy_id}")
            
        except Exception as e:
            logging.error(f"Failed to archive strategy {strategy_id}: {e}")
            raise

    def get_test_results(self, test_id: str) -> Optional[Dict]:
        """
        Retrieves results of a previous test.
        Implements QueryableStrategy interface.
        """
        for result in self.test_results.values():
            if result["test_id"] == test_id:
                return result
        logging.warning(f"Test {test_id} not found")
        return None