from abc import abstractmethod

import polars as pl

from src.factor.base_factor import BaseFactor


class FactorAggregator(BaseFactor):
    def __init__(self, security_universe, factor_type):
        super().__init__(security_universe, factor_type)
        self.sectors = self.get_internal_sectors()

    @abstractmethod
    def get_internal_sectors(self):
        pass

    @abstractmethod
    def get_fund_list(self, date):
        pass

    def get_sector_scores(self, observe_date):
        sector_score_list = []
        for sector in self.sectors:
            sector_score_df = sector.impl_sector_signal(observe_date)
            sector_score_df = sector_score_df.with_columns(
                pl.lit(sector.__class__.__name__).alias("class_name")
            ).select(
                pl.col("sector"),
                pl.col("date"),
                pl.col("z-score"),
                pl.col("class_name"),
            )
            sector_score_list.append(sector_score_df)
        sector_score_df = pl.concat(sector_score_list)
        return sector_score_df
