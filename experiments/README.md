# Experimental contract

All included generators produce synthetic measurements. They do not emulate a validated RP Hand or establish biological meridian mechanisms. Save source, configuration, seed, units, software revision and evaluation split with every result.

Train, validation and test sessions/objects are disjoint. Tune only on training/validation. Freeze the selected configuration before reporting test performance. Report unsuccessful models alongside successful ones. Test cases verify implementation properties; benchmark results assess behavior on the declared generator.

Real data must come from calibrated sensors with independent event labels and synchronized timestamps. No code in this release may command a physical hand.
