	net.imagej.ops.morphology.thin.ThinGuoHall(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.morphology.thin.ThinHilditch(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.morphology.thin.ThinMorphological(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.morphology.thin.ThinZhangSuen(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(IterableInterval out?) =
	net.imagej.ops.morphology.topHat.ListTopHat(
		IterableInterval out?,
		RandomAccessibleInterval in1,
		List in2)
	(Object out) =
	net.imagej.ops.run.RunByName(
		String in,
		Object[] args)
	(Object out) =
	net.imagej.ops.run.RunByOp(
		Op in,
		Object[] args)
	(Object out) =
	net.imagej.ops.run.RunByType(
		Class in,
		Object[] args)
	(List out) =
	net.imagej.ops.segment.detectJunctions.DefaultDetectJunctions(
		List in,
		double threshold?)
	(List out) =
	net.imagej.ops.segment.detectRidges.DefaultDetectRidges(
		RandomAccessibleInterval in,
		double width,
		double lowerThreshold,
		double higherThreshold,
		int ridgeLengthMin)
	(DoubleType out) =
	net.imagej.ops.stats.IntegralMean(
		DoubleType out,
		RectangleNeighborhood in)
	(DoubleType out?) =
	net.imagej.ops.stats.IntegralSum(
		DoubleType out?,
		RectangleNeighborhood in)
	(DoubleType out) =
	net.imagej.ops.stats.IntegralVariance(
		DoubleType out,
		RectangleNeighborhood in)
	(Matrix4d out) =
	net.imagej.ops.stats.regression.leastSquares.Quadric(
		Collection in)
	net.imagej.ops.thread.chunker.DefaultChunker(
		Chunk chunkable,
		long numberOfElements)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Huang(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$IJ1(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Intermodes(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$IsoData(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Li(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$MaxEntropy(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$MaxLikelihood(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Mean(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$MinError(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Minimum(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Moments(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Otsu(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Percentile(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$RenyiEntropy(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Rosin(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Shanbhag(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Triangle(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Yen(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalHuangThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalIJ1Threshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalIntermodesThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalIsoDataThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalLiThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalMaxEntropyThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalMaxLikelihoodThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalMinErrorThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalMinimumThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalMomentsThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalOtsuThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalPercentileThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalRenyiEntropyThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalRosinThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalShanbhagThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalTriangleThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalYenThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out?) =
	net.imagej.ops.threshold.apply.ApplyManualThreshold(
		IterableInterval out?,
		IterableInterval in,
		RealType threshold)
	(BitType out) =
	net.imagej.ops.threshold.apply.ApplyThresholdComparable(
		BitType out,
		Comparable in1,
		Object in2)
	(BitType out) =
	net.imagej.ops.threshold.apply.ApplyThresholdComparator(
		BitType out,
		Object in1,
		Object in2,
		Comparator comparator)
	(IterableInterval out) =
	net.imagej.ops.threshold.localBernsen.LocalBernsenThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double contrastThreshold,
		double halfMaxValue)
	(IterableInterval out) =
	net.imagej.ops.threshold.localContrast.LocalContrastThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.localMedian.LocalMedianThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c)
	(IterableInterval out) =
	net.imagej.ops.threshold.localMidGrey.LocalMidGreyThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c)
	(List out) =
	net.imagej.ops.topology.BoxCount(
		RandomAccessibleInterval in,
		Long maxSize?,
		Long minSize?,
		Double scaling?,
		Long gridMoves?)
	(DoubleType out?) =
	net.imagej.ops.topology.eulerCharacteristic.EulerCharacteristic26N(
		DoubleType out?,
		RandomAccessibleInterval in)
	(DoubleType out?) =
	net.imagej.ops.topology.eulerCharacteristic.EulerCharacteristic26NFloating(
		DoubleType out?,
		RandomAccessibleInterval in)
	(DoubleType out?) =
	net.imagej.ops.topology.eulerCharacteristic.EulerCorrection(
		DoubleType out?,
		RandomAccessibleInterval in)
	(CompositeIntervalView out) =
	net.imagej.ops.transform.collapseNumericView.DefaultCollapseNumeric2CompositeIntervalView(
		RandomAccessibleInterval in)
	(CompositeView out) =
	net.imagej.ops.transform.collapseNumericView.DefaultCollapseNumeric2CompositeView(
		RandomAccessible in,
		int numChannels)
	(CompositeIntervalView out) =
	net.imagej.ops.transform.collapseRealView.DefaultCollapseReal2CompositeIntervalView(
		RandomAccessibleInterval in)
	(CompositeView out) =
	net.imagej.ops.transform.collapseRealView.DefaultCollapseReal2CompositeView(
		RandomAccessible in,
		int numChannels)
	(CompositeIntervalView out) =
	net.imagej.ops.transform.collapseView.DefaultCollapse2CompositeIntervalView(
		RandomAccessibleInterval in)
	(CompositeView out) =
	net.imagej.ops.transform.collapseView.DefaultCollapse2CompositeView(
		RandomAccessible in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.concatenateView.ConcatenateViewWithAccessMode(
		List in,
		int concatenationAxis,
		StackAccessMode stackAccessMode)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.concatenateView.DefaultConcatenateView(
		List in,
		int concatenationAxis)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.dropSingletonDimensionsView.DefaultDropSingletonDimensionsView(
		RandomAccessibleInterval in)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendBorderView.DefaultExtendBorderView(
		RandomAccessibleInterval in)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendMirrorDoubleView.DefaultExtendMirrorDoubleView(
		RandomAccessibleInterval in)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendMirrorSingleView.DefaultExtendMirrorSingleView(
		RandomAccessibleInterval in)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendPeriodicView.DefaultExtendPeriodicView(
		RandomAccessibleInterval in)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendRandomView.DefaultExtendRandomView(
		RandomAccessibleInterval in,
		double min,
		double max)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendValueView.DefaultExtendValueView(
		RandomAccessibleInterval in,
		Type value)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendView.DefaultExtendView(
		RandomAccessibleInterval in,
		OutOfBoundsFactory factory)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendZeroView.DefaultExtendZeroView(
		RandomAccessibleInterval in)
	(IterableInterval out) =
	net.imagej.ops.transform.flatIterableView.DefaultFlatIterableView(
		RandomAccessibleInterval in)
	(MixedTransformView out) =
	net.imagej.ops.transform.hyperSliceView.DefaultHyperSliceView(
		RandomAccessible in,
		int d,
		long pos)
	(RealRandomAccessible out) =
	net.imagej.ops.transform.interpolateView.DefaultInterpolateView(
		EuclideanSpace in,
		InterpolatorFactory factory)
	(IntervalView out) =
	net.imagej.ops.transform.intervalView.DefaultIntervalView(
		RandomAccessible in,
		Interval interval)
	(IntervalView out) =
	net.imagej.ops.transform.intervalView.IntervalViewMinMax(
		RandomAccessible in,
		long[] min,
		long[] max)
	(MixedTransformView out) =
	net.imagej.ops.transform.invertAxisView.DefaultInvertAxisView(
		RandomAccessible in,
		int d)
	(MixedTransformView out) =
	net.imagej.ops.transform.offsetView.DefaultOffsetView(
		RandomAccessible in,
		long[] offset)
	(IntervalView out) =
	net.imagej.ops.transform.offsetView.OffsetViewInterval(
		RandomAccessible in,
		Interval interval)
	(IntervalView out) =
	net.imagej.ops.transform.offsetView.OffsetViewOriginSize(
		RandomAccessible in,
		long[] origin,
		long[] dimension)
	(IntervalView out) =
	net.imagej.ops.transform.permuteCoordinatesInverseView.DefaultPermuteCoordinatesInverseView(
		RandomAccessibleInterval in,
		int[] permutation)
	(IntervalView out) =
	net.imagej.ops.transform.permuteCoordinatesInverseView.PermuteCoordinateInverseViewOfDimension(
		RandomAccessibleInterval in,
		int[] permutation,
		int d)
	(IntervalView out) =
	net.imagej.ops.transform.permuteCoordinatesView.DefaultPermuteCoordinatesView(
		RandomAccessibleInterval in,
		int[] permutation)
	(IntervalView out) =
	net.imagej.ops.transform.permuteCoordinatesView.PermuteCoordinatesViewOfDimension(
		RandomAccessibleInterval in,
		int[] permutation,
		int d)
	(MixedTransformView out) =
	net.imagej.ops.transform.permuteView.DefaultPermuteView(
		RandomAccessible in,
		int fromAxis,
		int toAxis)
	(RandomAccessibleOnRealRandomAccessible out) =
	net.imagej.ops.transform.rasterView.DefaultRasterView(
		RealRandomAccessible in)
	(MixedTransformView out) =
	net.imagej.ops.transform.rotateView.DefaultRotateView(
		RandomAccessible in,
		int fromAxis,
		int toAxis)
	(TransformView out) =
	net.imagej.ops.transform.shearView.DefaultShearView(
		RandomAccessible in,
		int shearDimension,
		int referenceDimension)
	(IntervalView out) =
	net.imagej.ops.transform.shearView.ShearViewInterval(
		RandomAccessible in,
		Interval interval,
		int shearDimension,
		int referenceDimension)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.stackView.DefaultStackView(
		List in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.stackView.StackViewWithAccessMode(
		List in,
		StackAccessMode stackAccessMode)
	(SubsampleView out) =
	net.imagej.ops.transform.subsampleView.DefaultSubsampleView(
		RandomAccessible in,
		long step)
	(SubsampleView out) =
	net.imagej.ops.transform.subsampleView.SubsampleViewStepsForDims(
		RandomAccessible in,
		long[] steps)
	(MixedTransformView out) =
	net.imagej.ops.transform.translateView.DefaultTranslateView(
		RandomAccessible in,
		long[] translation)
	(TransformView out) =
	net.imagej.ops.transform.unshearView.DefaultUnshearView(
		RandomAccessible in,
		int shearDimension,
		int referenceDimension)
	(IntervalView out) =
	net.imagej.ops.transform.unshearView.UnshearViewInterval(
		RandomAccessible in,
		Interval interval,
		int shearDimension,
		int referenceDimension)
	(IntervalView out) =
	net.imagej.ops.transform.zeroMinView.DefaultZeroMinView(
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.structure.SingleStructureTensorEigenvaluesFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma,
		double integrationScale)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.structure.StructureTensorEigenvaluesFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.stats.SingleVarianceFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double radius)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.stats.VarianceFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(BitType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToBit(
		BitType out?,
		ComplexType in)
	(ComplexFloatType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToCfloat32(
		ComplexFloatType out?,
		ComplexType in)
	(ComplexDoubleType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToCfloat64(
		ComplexDoubleType out?,
		ComplexType in)
	(FloatType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToFloat32(
		FloatType out?,
		ComplexType in)
	(DoubleType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToFloat64(
		DoubleType out?,
		ComplexType in)
	(ShortType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToInt16(
		ShortType out?,
		ComplexType in)
	(IntType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToInt32(
		IntType out?,
		ComplexType in)
	(LongType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToInt64(
		LongType out?,
		ComplexType in)
	(ByteType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToInt8(
		ByteType out?,
		ComplexType in)
	(Unsigned12BitType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint12(
		Unsigned12BitType out?,
		ComplexType in)
	(Unsigned128BitType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint128(
		Unsigned128BitType out?,
		ComplexType in)
	(UnsignedShortType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint16(
		UnsignedShortType out?,
		ComplexType in)
	(Unsigned2BitType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint2(
		Unsigned2BitType out?,
		ComplexType in)
	(UnsignedIntType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint32(
		UnsignedIntType out?,
		ComplexType in)
	(Unsigned4BitType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint4(
		Unsigned4BitType out?,
		ComplexType in)
	(UnsignedLongType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint64(
		UnsignedLongType out?,
		ComplexType in)
	(UnsignedByteType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint8(
		UnsignedByteType out?,
		ComplexType in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelBiGauss.CreateKernel2ndDerivBiGaussDoubleType(
		double[] in1,
		Integer in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelBiGauss.DefaultCreateKernel2ndDerivBiGauss(
		double[] in1,
		Integer in2,
		ComplexType typeVar)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelBiGauss.DefaultCreateKernelBiGauss(
		double[] in1,
		Integer in2,
		ComplexType typeVar)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelBiGauss.CreateKernelBiGaussDoubleType(
		double[] in1,
		Integer in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.DefaultCreateKernelGabor(
		double[] in1,
		double[] in2,
		ComplexType typeVar)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.CreateKernelGaborIsotropic(
		Double in1,
		double[] in2,
		ComplexType typeVar)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.CreateKernelGaborComplexDoubleType(
		double[] in1,
		double[] in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.CreateKernelGaborIsotropicComplexDoubleType(
		Double in1,
		double[] in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.CreateKernelGaborIsotropicDoubleType(
		Double in1,
		double[] in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.CreateKernelGaborDoubleType(
		double[] in1,
		double[] in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelSobel.CreateKernelSobel(
		ComplexType type)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndIIToIIParallel(
		IterableInterval out,
		IterableInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndIIToRAIParallel(
		RandomAccessibleInterval out,
		IterableInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndRAIToIIParallel(
		IterableInterval out,
		IterableInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndRAIToRAIParallel(
		RandomAccessibleInterval out,
		IterableInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndIIToIIParallel(
		IterableInterval out,
		RandomAccessibleInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$IIAndIIParallel(
		IterableInterval arg,
		IterableInterval in,
		BinaryInplace1Op op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndIIToRAIParallel(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$IIAndRAIParallel(
		IterableInterval arg,
		RandomAccessibleInterval in,
		BinaryInplace1Op op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndRAIToIIParallel(
		IterableInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(RandomAccessibleInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$RAIAndIIParallel(
		RandomAccessibleInterval arg,
		IterableInterval in,
		BinaryInplace1Op op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapIIAndIIInplaceParallel(
		IterableInterval arg,
		IterableInterval in,
		BinaryInplaceOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndIIToII(
		IterableInterval out,
		IterableInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndIIToRAI(
		RandomAccessibleInterval out,
		IterableInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndRAIToII(
		IterableInterval out,
		IterableInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapIIInplaceParallel(
		IterableInterval arg,
		UnaryInplaceOp op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndRAIToRAI(
		RandomAccessibleInterval out,
		IterableInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndIIToII(
		IterableInterval out,
		RandomAccessibleInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$IIAndII(
		IterableInterval arg,
		IterableInterval in,
		BinaryInplace1Op op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndIIToRAI(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$IIAndRAI(
		IterableInterval arg,
		RandomAccessibleInterval in,
		BinaryInplace1Op op)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.integral.DefaultIntegralImg(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.integral.SquareIntegralImg(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndRAIToII(
		IterableInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(RandomAccessibleInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$RAIAndII(
		RandomAccessibleInterval arg,
		IterableInterval in,
		BinaryInplace1Op op)
	(IterableInterval out) =
	net.imagej.ops.map.MapNullaryII(
		IterableInterval out,
		NullaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.neighborhood.MapNeighborhoodWithCenter(
		IterableInterval out,
		RandomAccessibleInterval in1,
		Shape in2,
		CenterAwareComputerOp op)
	(ImgPlus out) =
	net.imagej.ops.transform.crop.CropImgPlus(
		ImgPlus in1,
		Interval in2,
		boolean dropSingleDimensions?)
	(IterableInterval out) =
	net.imagej.ops.transform.project.DefaultProjectParallel(
		IterableInterval out,
		RandomAccessibleInterval in,
		UnaryComputerOp method,
		int dim)
	(RealType out?) =
	net.imagej.ops.stats.DefaultMean(
		RealType out?,
		Iterable in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.deconvolve.NonCirculantFirstGuess(
		RandomAccessibleInterval in,
		RealType outType,
		Dimensions k)
	(RandomAccessibleInterval arg) =
	net.imagej.ops.deconvolve.NonCirculantNormalizationFactor(
		RandomAccessibleInterval arg,
		Dimensions k,
		Dimensions l,
		RandomAccessibleInterval fftInput,
		RandomAccessibleInterval fftKernel)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.FFTMethodsLinearFFTFilterC(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		RandomAccessibleInterval fftInput?,
		RandomAccessibleInterval fftKernel?,
		boolean performInputFFT?,
		boolean performKernelFFT?,
		BinaryComputerOp frequencyOp)
	(IterableInterval out) =
	net.imagej.ops.filter.addPoissonNoise.AddPoissonNoiseMap(
		IterableInterval out,
		IterableInterval in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.convolve.ConvolveFFTC(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		RandomAccessibleInterval fftInput?,
		RandomAccessibleInterval fftKernel?,
		boolean performInputFFT?,
		boolean performKernelFFT?)
	(IterableInterval out) =
	net.imagej.ops.filter.max.DefaultMaxFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.filter.mean.DefaultMeanFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.filter.median.DefaultMedianFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.filter.min.DefaultMinFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.filter.sigma.DefaultSigmaFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		Double range,
		Double minPixelFraction)
	(IterableInterval out) =
	net.imagej.ops.filter.variance.DefaultVarianceFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.image.integral.WrappedIntegralImg(
		RandomAccessibleInterval in)
	(IterableInterval arg) =
	net.imagej.ops.map.MapIIAndIIInplace(
		IterableInterval arg,
		IterableInterval in,
		BinaryInplaceOp op)
	(Iterable arg) =
	net.imagej.ops.map.MapIterableInplace(
		Iterable arg,
		UnaryInplaceOp op)
	(Iterable out) =
	net.imagej.ops.map.MapNullaryIterable(
		Iterable out,
		NullaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.neighborhood.DefaultMapNeighborhood(
		IterableInterval out,
		RandomAccessibleInterval in1,
		Shape in2,
		UnaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.math.multiply.ComplexConjugateMultiplyMap(
		IterableInterval out,
		IterableInterval in1,
		IterableInterval in2)
	(ComplexType out) =
	net.imagej.ops.math.multiply.ComplexConjugateMultiplyOp(
		ComplexType out,
		ComplexType in1,
		ComplexType in2)
	(IterableInterval out?) =
	net.imagej.ops.morphology.dilate.ListDilate(
		IterableInterval out?,
		RandomAccessibleInterval in1,
		List in2,
		boolean isFull?)
	(IterableInterval out?) =
	net.imagej.ops.morphology.erode.ListErode(
		IterableInterval out?,
		RandomAccessibleInterval in1,
		List in2,
		boolean isFull?)
	(IterableInterval out) =
	net.imagej.ops.threshold.localMean.LocalMeanThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c)
	(IterableInterval out) =
	net.imagej.ops.threshold.localNiblack.LocalNiblackThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c,
		double k)
	(IterableInterval out) =
	net.imagej.ops.threshold.localPhansalkar.LocalPhansalkarThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double k?,
		double r?)
	(IterableInterval out) =
	net.imagej.ops.threshold.localSauvola.LocalSauvolaThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double k?,
		double r?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.crop.CropRAI(
		RandomAccessibleInterval in1,
		Interval in2,
		boolean dropSingleDimensions?)
	(IterableInterval out) =
	net.imagej.ops.transform.project.ProjectRAIToII(
		IterableInterval out,
		RandomAccessibleInterval in,
		UnaryComputerOp method,
		int dim)
	(IterableInterval out) =
	net.imagej.ops.transform.project.ProjectRAIToIterableInterval(
		IterableInterval out,
		RandomAccessibleInterval in,
		UnaryComputerOp method,
		int dim)
	(Iterable out) =
	net.imagej.ops.map.MapIterableToIterable(
		Iterable out,
		Iterable in,
		UnaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.threshold.localMean.LocalMeanThresholdIntegral(
		IterableInterval out,
		RandomAccessibleInterval in,
		RectangleShape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c)
	(IterableInterval out) =
	net.imagej.ops.threshold.localNiblack.LocalNiblackThresholdIntegral(
		IterableInterval out,
		RandomAccessibleInterval in,
		RectangleShape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c,
		double k)
	(IterableInterval out) =
	net.imagej.ops.threshold.localPhansalkar.LocalPhansalkarThresholdIntegral(
		IterableInterval out,
		RandomAccessibleInterval in,
		RectangleShape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double k?,
		double r?)
	(IterableInterval out) =
	net.imagej.ops.threshold.localSauvola.LocalSauvolaThresholdIntegral(
		IterableInterval out,
		RandomAccessibleInterval in,
		RectangleShape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double k?,
		double r?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.math.ConstantToIIOutputRAI$Add(
		RandomAccessibleInterval out,
		IterableInterval in,
		NumericType value)
	(RandomAccessibleInterval out) =
	net.imagej.ops.math.ConstantToIIOutputRAI$Divide(
		RandomAccessibleInterval out,
		IterableInterval in,
		NumericType value)
	(RandomAccessibleInterval out) =
	net.imagej.ops.math.ConstantToIIOutputRAI$Multiply(
		RandomAccessibleInterval out,
		IterableInterval in,
		NumericType value)
	(RandomAccessibleInterval out) =
	net.imagej.ops.math.ConstantToIIOutputRAI$Subtract(
		RandomAccessibleInterval out,
		IterableInterval in,
		NumericType value)
	net.imagej.ops.thread.chunker.ChunkerInterleaved(
		Chunk chunkable,
		long numberOfElements)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.distancetransform.DefaultDistanceTransform(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.distancetransform.DefaultDistanceTransformCalibration(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		double[] calibration)
Started !help.py at Wed Apr 17 12:49:02 CDT 2024
Started !help.py at Wed Apr 17 12:49:11 CDT 2024
Started !help.py at Wed Apr 17 12:49:30 CDT 2024
Started !help.py at Wed Apr 17 12:49:43 CDT 2024
Available operations:
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultVerticesCountPolygon(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultVerticesCountConvexHullPolygon(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultConvexityPolygon(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultBoundarySizeConvexHullPolygon(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultBoxivityPolygon(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultSizeConvexHullPolygon(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultSolidityPolygon(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultBoxivityMesh(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultCompactness(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultVerticesCountConvexHullMesh(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultVolumeConvexHullMesh(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultConvexityMesh(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultMainElongation(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultMedianElongation(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultSolidityMesh(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultSparenessMesh(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultSphericity(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultSurfaceArea(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultSurfaceAreaConvexHullMesh(
		DoubleType out?,
		Mesh in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom3d.DefaultVerticesCountMesh(
		DoubleType out?,
		Mesh in)
	(DoubleType out) =
	net.imagej.ops.geom.SizeII(
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.IterableCentralMoment00(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.DefaultCentralMoment01(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.DefaultCentralMoment10(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.IterableCentralMoment11(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.moments.DefaultMoment00(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.moments.DefaultMoment01(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.moments.DefaultMoment10(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.moments.DefaultMoment11(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.stats.IterableGeometricMean(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.IterableHarmonicMean(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.IterableMax(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.IterableMean(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.IterableMin(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.IISize(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.stats.IterableStandardDeviation(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.IterableVariance(
		RealType out?,
		Iterable in)
	(ArrayImg out?) =
	net.imagej.ops.copy.CopyArrayImg(
		ArrayImg out?,
		ArrayImg in)
	(LabelingMapping out?) =
	net.imagej.ops.copy.CopyLabelingMapping(
		LabelingMapping out?,
		LabelingMapping in)
	(Img out) =
	net.imagej.ops.create.img.CreateImgFromImg(
		Img in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.correlate.PadAndCorrelateFFT(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		long[] borderSize?,
		OutOfBoundsFactory obfInput?,
		OutOfBoundsFactory obfKernel?,
		RealType outType?,
		ComplexType fftType?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.slice.SliceRAI2RAI(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in,
		UnaryComputerOp op,
		int[] axisIndices,
		boolean dropSingleDimensions?)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultSizePolygon(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out) =
	net.imagej.ops.geom.geom3d.DefaultVolumeMesh(
		Mesh in)
	(Img out) =
	net.imagej.ops.create.img.CreateImgFromII(
		IterableInterval in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.convolve.ConvolveNaiveF(
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		OutOfBoundsFactory obf?,
		RealType outType?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.convolve.PadAndConvolveFFTF(
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		OutOfBoundsFactory obf?,
		RealType outType?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.pad.PadShiftKernel(
		RandomAccessibleInterval in1,
		Dimensions in2)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$AddByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$AddDouble(
		ArrayImg arg,
		double value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$AddFloat(
		ArrayImg arg,
		float value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$AddInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$AddLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$AddShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$AddUnsignedByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$AddUnsignedInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$AddUnsignedLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$AddUnsignedShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$DivideByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$DivideDouble(
		ArrayImg arg,
		double value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$DivideFloat(
		ArrayImg arg,
		float value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$DivideInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$DivideLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$DivideShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$DivideUnsignedByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$DivideUnsignedInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$DivideUnsignedLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$DivideUnsignedShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$MultiplyByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$MultiplyDouble(
		ArrayImg arg,
		double value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$MultiplyFloat(
		ArrayImg arg,
		float value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$MultiplyInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$MultiplyLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$MultiplyShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$MultiplyUnsignedByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$MultiplyUnsignedInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$MultiplyUnsignedLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$MultiplyUnsignedShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$SubtractByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$SubtractDouble(
		ArrayImg arg,
		double value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$SubtractFloat(
		ArrayImg arg,
		float value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$SubtractInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$SubtractLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$SubtractShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$SubtractUnsignedByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$SubtractUnsignedInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$SubtractUnsignedLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImageP$SubtractUnsignedShort(
		ArrayImg arg,
		short value)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.scaleView.DefaultScaleView(
		RandomAccessibleInterval in,
		double[] scaleFactors,
		InterpolatorFactory interpolator,
		OutOfBoundsFactory outOfBoundsFactory?)
	(Img out) =
	net.imagej.ops.create.img.CreateImgFromRAI(
		RandomAccessibleInterval in)
	(ImgFactory out) =
	net.imagej.ops.create.imgFactory.CreateImgFactoryFromImg(
		Img in)
	(ImgLabeling out) =
	net.imagej.ops.create.imgLabeling.CreateImgLabelingFromInterval(
		Interval in,
		IntegerType outType?,
		ImgFactory fac?,
		int maxNumLabelSets?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.deconvolve.PadAndRichardsonLucy(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		long[] borderSize?,
		OutOfBoundsFactory obfInput?,
		OutOfBoundsFactory obfKernel?,
		RealType outType?,
		ComplexType fftType?,
		int maxIterations,
		boolean nonCirculant?,
		boolean accelerate?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.deconvolve.PadAndRichardsonLucyTV(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		long[] borderSize?,
		OutOfBoundsFactory obfInput?,
		OutOfBoundsFactory obfKernel?,
		RealType outType?,
		ComplexType fftType?,
		int maxIterations,
		boolean nonCirculant?,
		boolean accelerate?,
		float regularizationFactor)
	(RandomAccessibleInterval out) =
	net.imagej.ops.deconvolve.RichardsonLucyC(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		RandomAccessibleInterval fftInput?,
		RandomAccessibleInterval fftKernel?,
		boolean performInputFFT?,
		boolean performKernelFFT?,
		int maxIterations,
		UnaryInplaceOp accelerator?,
		UnaryComputerOp updateOp?,
		RandomAccessibleInterval raiExtendedEstimate?,
		ArrayList iterativePostProcessingOps?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.deconvolve.RichardsonLucyCorrection(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		RandomAccessibleInterval fftBuffer,
		RandomAccessibleInterval fftKernel)
	(RandomAccessibleInterval out) =
	net.imagej.ops.deconvolve.RichardsonLucyTVUpdate(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in,
		float regularizationFactor,
		RandomAccessibleInterval variation?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.deconvolve.RichardsonLucyUpdate(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in)
	(RealType out?) =
	net.imagej.ops.filter.addNoise.AddNoiseRealTypeCFI(
		RealType out?,
		RealType in,
		double rangeMin,
		double rangeMax,
		double rangeStdDev,
		long seed?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.fft.FFTMethodsOpF(
		RandomAccessibleInterval in,
		long[] borderSize?,
		boolean fast?,
		OutOfBoundsFactory obf?,
		ComplexType fftType?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.gauss.DefaultGaussRA(
		RandomAccessibleInterval out,
		RandomAccessible in,
		double[] sigmas)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.filter.gauss.GaussRAISingleSigma(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		double sigma,
		OutOfBoundsFactory outOfBounds?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.pad.DefaultPadShiftKernelFFT(
		RandomAccessibleInterval in1,
		Dimensions in2,
		boolean fast?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.pad.PadInputFFTMethods(
		RandomAccessibleInterval in1,
		Dimensions in2,
		boolean fast?,
		OutOfBoundsFactory obf?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.pad.PadShiftKernelFFTMethods(
		RandomAccessibleInterval in1,
		Dimensions in2,
		boolean fast?)
	(String help) =
	net.imagej.ops.help.HelpForNamespace(
		Namespace namespace)
	(String help) =
	net.imagej.ops.help.HelpForOp(
		Op op)
	(IterableInterval out) =
	net.imagej.ops.image.invert.InvertIIInteger(
		IterableInterval out,
		IterableInterval in,
		IntegerType min?,
		IntegerType max?)
	(ImgLabeling out?) =
	net.imagej.ops.labeling.MergeLabeling(
		ImgLabeling out?,
		ImgLabeling in1,
		ImgLabeling in2,
		RandomAccessibleInterval mask?)
	(IterableInterval out) =
	net.imagej.ops.map.MapViewIIToII(
		IterableInterval in,
		UnaryComputerOp op,
		Type type)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$AddByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$AddDouble(
		ArrayImg arg,
		double value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$AddFloat(
		ArrayImg arg,
		float value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$AddInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$AddLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$AddShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$AddUnsignedByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$AddUnsignedInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$AddUnsignedLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$AddUnsignedShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$DivideByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$DivideDouble(
		ArrayImg arg,
		double value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$DivideFloat(
		ArrayImg arg,
		float value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$DivideInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$DivideLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$DivideShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$DivideUnsignedByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$DivideUnsignedInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$DivideUnsignedLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$DivideUnsignedShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$MultiplyByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$MultiplyDouble(
		ArrayImg arg,
		double value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$MultiplyFloat(
		ArrayImg arg,
		float value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$MultiplyInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$MultiplyLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$MultiplyShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$MultiplyUnsignedByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$MultiplyUnsignedInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$MultiplyUnsignedLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$MultiplyUnsignedShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$SubtractByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$SubtractDouble(
		ArrayImg arg,
		double value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$SubtractFloat(
		ArrayImg arg,
		float value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$SubtractInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$SubtractLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$SubtractShort(
		ArrayImg arg,
		short value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$SubtractUnsignedByte(
		ArrayImg arg,
		byte value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$SubtractUnsignedInt(
		ArrayImg arg,
		int value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$SubtractUnsignedLong(
		ArrayImg arg,
		long value)
	(ArrayImg arg) =
	net.imagej.ops.math.ConstantToArrayImage$SubtractUnsignedShort(
		ArrayImg arg,
		short value)
	(IterableInterval out?) =
	net.imagej.ops.math.IIToIIOutputII$Add(
		IterableInterval out?,
		IterableInterval in1,
		IterableInterval in2)
	(IterableInterval out?) =
	net.imagej.ops.math.IIToIIOutputII$Divide(
		IterableInterval out?,
		IterableInterval in1,
		IterableInterval in2)
	(IterableInterval out?) =
	net.imagej.ops.math.IIToIIOutputII$Multiply(
		IterableInterval out?,
		IterableInterval in1,
		IterableInterval in2)
	(IterableInterval out?) =
	net.imagej.ops.math.IIToIIOutputII$Subtract(
		IterableInterval out?,
		IterableInterval in1,
		IterableInterval in2)
	(NumericType out?) =
	net.imagej.ops.math.NumericTypeBinaryMath$Add(
		NumericType out?,
		NumericType in1,
		NumericType in2)
	(NumericType out?) =
	net.imagej.ops.math.NumericTypeBinaryMath$Divide(
		NumericType out?,
		NumericType in1,
		NumericType in2)
	(NumericType out?) =
	net.imagej.ops.math.NumericTypeBinaryMath$Multiply(
		NumericType out?,
		NumericType in1,
		NumericType in2)
	(NumericType out?) =
	net.imagej.ops.math.NumericTypeBinaryMath$Subtract(
		NumericType out?,
		NumericType in1,
		NumericType in2)
	(Iterable out) =
	net.imagej.ops.threshold.apply.ApplyConstantThreshold(
		Iterable out,
		Iterable in1,
		RealType in2)
	(RealType out?) =
	net.imagej.ops.threshold.huang.ComputeHuangThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.ij1.ComputeIJ1Threshold(
		RealType out?,
		Histogram1d in)
	(RealType out?,
		String errMsg) =
	net.imagej.ops.threshold.intermodes.ComputeIntermodesThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?,
		String errMsg) =
	net.imagej.ops.threshold.isoData.ComputeIsoDataThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.li.ComputeLiThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.maxEntropy.ComputeMaxEntropyThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?,
		String errMsg) =
	net.imagej.ops.threshold.maxLikelihood.ComputeMaxLikelihoodThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.mean.ComputeMeanThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?,
		String errMsg) =
	net.imagej.ops.threshold.minError.ComputeMinErrorThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?,
		String errMsg) =
	net.imagej.ops.threshold.minimum.ComputeMinimumThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.moments.ComputeMomentsThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.otsu.ComputeOtsuThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.percentile.ComputePercentileThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.renyiEntropy.ComputeRenyiEntropyThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.rosin.ComputeRosinThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.shanbhag.ComputeShanbhagThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.triangle.ComputeTriangleThreshold(
		RealType out?,
		Histogram1d in)
	(RealType out?) =
	net.imagej.ops.threshold.yen.ComputeYenThreshold(
		RealType out?,
		Histogram1d in)
	(IntervalView out) =
	net.imagej.ops.transform.hyperSliceView.IntervalHyperSliceView(
		RandomAccessibleInterval in,
		int d,
		long pos)
	(IntervalView out) =
	net.imagej.ops.transform.invertAxisView.IntervalInvertAxisView(
		RandomAccessibleInterval in,
		int d)
	(IntervalView out) =
	net.imagej.ops.transform.permuteView.IntervalPermuteView(
		RandomAccessibleInterval in,
		int fromAxis,
		int toAxis)
	(IntervalView out) =
	net.imagej.ops.transform.rotateView.IntervalRotateView(
		RandomAccessibleInterval in,
		int fromAxis,
		int toAxis)
	(SubsampleIntervalView out) =
	net.imagej.ops.transform.subsampleView.IntervalSubsampleView(
		RandomAccessibleInterval in,
		long step)
	(SubsampleIntervalView out) =
	net.imagej.ops.transform.subsampleView.SubsampleIntervalViewStepsForDims(
		RandomAccessibleInterval in,
		long[] steps)
	(IntervalView out) =
	net.imagej.ops.transform.translateView.IntervalTranslateView(
		RandomAccessibleInterval in,
		long[] translation)
	(BitType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToBit(
		BitType out?,
		IntegerType in)
	(ShortType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToInt16(
		ShortType out?,
		IntegerType in)
	(IntType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToInt32(
		IntType out?,
		IntegerType in)
	(LongType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToInt64(
		LongType out?,
		IntegerType in)
	(ByteType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToInt8(
		ByteType out?,
		IntegerType in)
	(Unsigned12BitType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToUint12(
		Unsigned12BitType out?,
		IntegerType in)
	(Unsigned128BitType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToUint128(
		Unsigned128BitType out?,
		IntegerType in)
	(UnsignedShortType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToUint16(
		UnsignedShortType out?,
		IntegerType in)
	(Unsigned2BitType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToUint2(
		Unsigned2BitType out?,
		IntegerType in)
	(UnsignedIntType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToUint32(
		UnsignedIntType out?,
		IntegerType in)
	(Unsigned4BitType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToUint4(
		Unsigned4BitType out?,
		IntegerType in)
	(UnsignedLongType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToUint64(
		UnsignedLongType out?,
		IntegerType in)
	(UnsignedByteType out?) =
	net.imagej.ops.convert.ConvertTypes$IntegerToUint8(
		UnsignedByteType out?,
		IntegerType in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.pad.PadInput(
		RandomAccessibleInterval in,
		Dimensions paddedDimensions,
		OutOfBoundsFactory obf?)
	(Interval out) =
	net.imagej.ops.filter.pad.PaddingIntervalCentered(
		RandomAccessibleInterval in1,
		Dimensions in2)
	(Interval out) =
	net.imagej.ops.filter.pad.PaddingIntervalOrigin(
		RandomAccessibleInterval in1,
		Interval in2)
	(IterableInterval out) =
	net.imagej.ops.map.MapUnaryComputers$IIToIIParallel(
		IterableInterval out,
		IterableInterval in,
		UnaryComputerOp op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapUnaryComputers$IIToRAIParallel(
		RandomAccessibleInterval out,
		IterableInterval in,
		UnaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapUnaryComputers$RAIToIIParallel(
		IterableInterval out,
		RandomAccessibleInterval in,
		UnaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapUnaryComputers$IIToII(
		IterableInterval out,
		IterableInterval in,
		UnaryComputerOp op)
	(RealLocalizable out) =
	net.imagej.ops.geom.CentroidLabelRegion(
		LabelRegion in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapUnaryComputers$IIToRAI(
		RandomAccessibleInterval out,
		IterableInterval in,
		UnaryComputerOp op)
	(IterableInterval out?) =
	net.imagej.ops.copy.CopyII(
		IterableInterval out?,
		IterableInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.copy.CopyRAI(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.filter.dog.DoGSingleSigmas(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		double sigma1,
		double sigma2,
		OutOfBoundsFactory fac?)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.filter.gauss.DefaultGaussRAI(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		double[] sigmas,
		OutOfBoundsFactory outOfBounds?)
	(RealLocalizable out) =
	net.imagej.ops.geom.CentroidII(
		IterableInterval in)
	(ImgLabeling out?) =
	net.imagej.ops.labeling.cca.DefaultCCA(
		ImgLabeling out?,
		RandomAccessibleInterval in,
		StructuringElement se,
		Iterator labelGenerator?)
	(IterableInterval out) =
	net.imagej.ops.map.MapUnaryComputers$RAIToII(
		IterableInterval out,
		RandomAccessibleInterval in,
		UnaryComputerOp op)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$BooleanAnd(
		boolean a,
		boolean b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$BooleanEqual(
		boolean a,
		boolean b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$BooleanNot(
		boolean a)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$BooleanNotEqual(
		boolean a,
		boolean b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$BooleanOr(
		boolean a,
		boolean b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$BooleanXor(
		boolean a,
		boolean b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$IntegerEqual(
		int a,
		int b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$IntegerGreaterThan(
		int a,
		int b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$IntegerGreaterThanOrEqual(
		int a,
		int b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$IntegerLessThan(
		int a,
		int b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$IntegerLessThanOrEqual(
		int a,
		int b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$IntegerNotEqual(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerAbs(
		int a)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerAdd(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerAnd(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerComplement(
		int a)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerDivide(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerLeftShift(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerMax(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerMin(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerMultiply(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerNegate(
		int a)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerOr(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerRemainder(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerRightShift(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerSubtract(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerUnsignedRightShift(
		int a,
		int b)
	(int result) =
	net.imagej.ops.math.PrimitiveMath$IntegerXor(
		int a,
		int b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$LongEqual(
		long a,
		long b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$LongGreaterThan(
		long a,
		long b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$LongGreaterThanOrEqual(
		long a,
		long b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$LongLessThan(
		long a,
		long b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$LongLessThanOrEqual(
		long a,
		long b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$LongNotEqual(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongAbs(
		long a)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongAdd(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongAnd(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongComplement(
		long a)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongDivide(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongLeftShift(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongMax(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongMin(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongMultiply(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongNegate(
		long a)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongOr(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongRemainder(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongRightShift(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongSubtract(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongUnsignedRightShift(
		long a,
		long b)
	(long result) =
	net.imagej.ops.math.PrimitiveMath$LongXor(
		long a,
		long b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$FloatEqual(
		float a,
		float b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$FloatGreaterThan(
		float a,
		float b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$FloatGreaterThanOrEqual(
		float a,
		float b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$FloatLessThan(
		float a,
		float b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$FloatLessThanOrEqual(
		float a,
		float b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$FloatNotEqual(
		float a,
		float b)
	(float result) =
	net.imagej.ops.math.PrimitiveMath$FloatAbs(
		float a)
	(float result) =
	net.imagej.ops.math.PrimitiveMath$FloatAdd(
		float a,
		float b)
	(float result) =
	net.imagej.ops.math.PrimitiveMath$FloatDivide(
		float a,
		float b)
	(float result) =
	net.imagej.ops.math.PrimitiveMath$FloatMax(
		float a,
		float b)
	(float result) =
	net.imagej.ops.math.PrimitiveMath$FloatMin(
		float a,
		float b)
	(float result) =
	net.imagej.ops.math.PrimitiveMath$FloatMultiply(
		float a,
		float b)
	(float result) =
	net.imagej.ops.math.PrimitiveMath$FloatNegate(
		float a)
	(float result) =
	net.imagej.ops.math.PrimitiveMath$FloatRemainder(
		float a,
		float b)
	(float result) =
	net.imagej.ops.math.PrimitiveMath$FloatRound(
		float a)
	(float result) =
	net.imagej.ops.math.PrimitiveMath$FloatSignum(
		float a)
	(float result) =
	net.imagej.ops.math.PrimitiveMath$FloatSubtract(
		float a,
		float b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$DoubleEqual(
		double a,
		double b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$DoubleGreaterThan(
		double a,
		double b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$DoubleGreaterThanOrEqual(
		double a,
		double b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$DoubleLessThan(
		double a,
		double b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$DoubleLessThanOrEqual(
		double a,
		double b)
	(boolean result) =
	net.imagej.ops.logic.PrimitiveLogic$DoubleNotEqual(
		double a,
		double b)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleAbs(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleAdd(
		double a,
		double b)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleArccos(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleArcsin(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleArctan(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleCeil(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleCos(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleCosh(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleCubeRoot(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleDivide(
		double a,
		double b)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleExp(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleFloor(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleLog(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleLog10(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleLogOnePlusX(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleMax(
		double a,
		double b)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleMin(
		double a,
		double b)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleMultiply(
		double a,
		double b)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleNegate(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoublePower(
		double a,
		double b)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleRemainder(
		double a,
		double b)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleRound(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleSignum(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleSin(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleSinh(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleSqrt(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleSubtract(
		double a,
		double b)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleTan(
		double a)
	(double result) =
	net.imagej.ops.math.PrimitiveMath$DoubleTanh(
		double a)
	(ArrayList out?) =
	net.imagej.ops.features.lbp2d.DefaultLBP2D(
		ArrayList out?,
		RandomAccessibleInterval in,
		int distance,
		int histogramSize)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.dog.SingleDifferenceOfGaussiansFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma1,
		double sigma2)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.dog.DifferenceOfGaussiansFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.gabor.SingleGaborFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma,
		double gamma,
		double psi,
		double frequency,
		int nAngles,
		boolean legacyNormalize)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.gabor.GaborFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		boolean legacyNormalize)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.gauss.SingleGaussFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.gauss.GaussFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultCircularity(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultEccentricity(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultElongation(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultFeretsAngle(
		DoubleType out?,
		Pair in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultFeretsDiameter(
		DoubleType out?,
		Pair in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultMajorAxis(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultMinorAxis(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultPerimeterLength(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultRoundness(
		DoubleType out?,
		Polygon2D in)
	(Polygon2D out) =
	net.imagej.ops.geom.geom2d.DefaultSmallestEnclosingRectangle(
		Polygon2D in)
	(Mesh out) =
	net.imagej.ops.geom.geom3d.mesh.DefaultSmallestOrientedBoundingBox(
		Mesh in)
	(RealLocalizable out) =
	net.imagej.ops.geom.CentroidPolygon(
		Polygon2D in)
	(RealLocalizable out) =
	net.imagej.ops.geom.CentroidMesh(
		Mesh in)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.gradient.SingleGradientFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.gradient.GradientFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultClusterPromenence(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultClusterShade(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultContrast(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultCorrelation(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultDifferenceEntropy(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultDifferenceVariance(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultEntropy(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultICM1(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultICM2(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultIFDM(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultMaxProbability(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultSumAverage(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultSumEntropy(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultSumVariance(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultTextureHomogeneity(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultVariance(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.hessian.SingleHessian3DFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma,
		boolean absoluteValues)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.hessian.SingleHessianFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.hessian.HessianFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.hessian.Hessian3DFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		boolean absoluteValues)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.DefaultCentralMoment00(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.DefaultCentralMoment02(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.DefaultCentralMoment03(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.DefaultCentralMoment11(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.DefaultCentralMoment12(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.DefaultCentralMoment20(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.DefaultCentralMoment21(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.centralmoments.DefaultCentralMoment30(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.hu.DefaultHuMoment1(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.hu.DefaultHuMoment2(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.hu.DefaultHuMoment3(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.hu.DefaultHuMoment4(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.hu.DefaultHuMoment5(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.hu.DefaultHuMoment6(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.hu.DefaultHuMoment7(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.normalizedcentralmoments.DefaultNormalizedCentralMoment02(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.normalizedcentralmoments.DefaultNormalizedCentralMoment03(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.normalizedcentralmoments.DefaultNormalizedCentralMoment11(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.normalizedcentralmoments.DefaultNormalizedCentralMoment12(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.normalizedcentralmoments.DefaultNormalizedCentralMoment20(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.normalizedcentralmoments.DefaultNormalizedCentralMoment21(
		RealType out?,
		IterableInterval in)
	(RealType out?) =
	net.imagej.ops.imagemoments.normalizedcentralmoments.DefaultNormalizedCentralMoment30(
		RealType out?,
		IterableInterval in)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.lipschitz.SingleLipschitzFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double slope,
		long border)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.lipschitz.LipschitzFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		long border)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.stats.SingleSphereShapedFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double radius,
		String operation)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.stats.SphereShapedFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		String operation)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.gradient.SingleSobelGradientFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.deprecated.gradient.SobelGradientFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RealType out?) =
	net.imagej.ops.stats.DefaultGeometricMean(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultHarmonicMean(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultKurtosis(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultMedian(
		RealType out?,
		Iterable in)
	(Pair out) =
	net.imagej.ops.stats.DefaultMinMax(
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultMoment1AboutMean(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultMoment2AboutMean(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultMoment3AboutMean(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultMoment4AboutMean(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultPercentile(
		RealType out?,
		Iterable in,
		double percent)
	(RealType out?) =
	net.imagej.ops.stats.DefaultQuantile(
		RealType out?,
		Iterable in,
		double quantile)
	(RealType out?) =
	net.imagej.ops.stats.DefaultSize(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultSkewness(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultStandardDeviation(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultSum(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultSumOfInverses(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultSumOfLogs(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultSumOfSquares(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.stats.DefaultVariance(
		RealType out?,
		Iterable in)
	(RealType out?) =
	net.imagej.ops.features.tamura2d.DefaultCoarsenessFeature(
		RealType out?,
		RandomAccessibleInterval in)
	(RealType out?) =
	net.imagej.ops.features.tamura2d.DefaultContrastFeature(
		RealType out?,
		RandomAccessibleInterval in)
	(RealType out?) =
	net.imagej.ops.features.tamura2d.DefaultDirectionalityFeature(
		RealType out?,
		RandomAccessibleInterval in,
		int histogramSize)
	(MixedTransformView out) =
	net.imagej.ops.transform.addDimensionView.DefaultAddDimensionView(
		RandomAccessible in)
	(IntervalView out) =
	net.imagej.ops.transform.addDimensionView.AddDimensionViewMinMax(
		RandomAccessibleInterval in,
		long minOfNewDim,
		long maxOfNewDim)
	(RealType out?) =
	net.imagej.ops.features.zernike.DefaultMagnitudeFeature(
		RealType out?,
		IterableInterval in,
		int order,
		int repitition)
	(RealType out?) =
	net.imagej.ops.features.zernike.DefaultPhaseFeature(
		RealType out?,
		IterableInterval in,
		int order,
		int repitition)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.dog2.SingleDifferenceOfGaussiansFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma1,
		double sigma2)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.dog2.DifferenceOfGaussiansFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.gauss.SingleGaussianBlurFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.gauss.GaussianBlurFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.gradient.SingleGaussianGradientMagnitudeFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.gradient.GaussianGradientMagnitudeFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.hessian.SingleHessianEigenvaluesFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.hessian.HessianEigenvaluesFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.laplacian.SingleLaplacianOfGaussianFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.laplacian.LaplacianOfGaussianFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.stats.SingleMaxFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double radius)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.stats.MaxFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.stats.SingleMeanFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double radius)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.stats.MeanFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.stats.SingleMinFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double radius)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.stats.MinFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.identity.IdentityFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(Double out) =
	net.imagej.ops.coloc.icq.LiICQ(
		Iterable in1,
		Iterable in2,
		DoubleType mean1?,
		DoubleType mean2?)
	(Double out) =
	net.imagej.ops.coloc.kendallTau.KendallTauBRank(
		Iterable in1,
		Iterable in2)
	(Double out) =
	net.imagej.ops.coloc.maxTKendallTau.MTKT(
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		long seed?)
	(PValueResult out) =
	net.imagej.ops.coloc.pValue.DefaultPValue(
		PValueResult out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		BinaryFunctionOp op,
		int nrRandomizations?,
		Dimensions psfSize?,
		long seed?)
	(Double out) =
	net.imagej.ops.coloc.pearsons.DefaultPearsons(
		Iterable in1,
		Iterable in2)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Bit(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Cfloat32(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Cfloat64(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Float32(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Float64(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Int16(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Int32(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Int64(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Int8(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Uint12(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Uint128(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Uint16(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Uint2(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Uint32(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Uint4(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Uint64(
		Img out?,
		IterableInterval in)
	(Img out?) =
	net.imagej.ops.convert.ConvertImages$Uint8(
		Img out?,
		IterableInterval in)
	(RealType out) =
	net.imagej.ops.convert.clip.ClipRealTypes(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.convert.copy.CopyRealTypes(
		RealType out,
		RealType in)
	(IterableInterval out) =
	net.imagej.ops.convert.imageType.ConvertIIs(
		IterableInterval out,
		IterableInterval in,
		RealTypeConverter pixConvert)
	(RealType out) =
	net.imagej.ops.convert.normalizeScale.NormalizeScaleRealTypes(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.convert.scale.ScaleRealTypes(
		RealType out,
		RealType in)
	(Img out?) =
	net.imagej.ops.copy.CopyImg(
		Img out?,
		Img in)
	(ImgLabeling out?) =
	net.imagej.ops.copy.CopyImgLabeling(
		ImgLabeling out?,
		ImgLabeling in)
	(Type out?) =
	net.imagej.ops.copy.CopyType(
		Type out?,
		Type in)
	(Img out) =
	net.imagej.ops.create.img.CreateImgFromDimsAndType(
		Dimensions in1,
		NativeType in2,
		ImgFactory factory?)
	(Img out) =
	net.imagej.ops.create.img.CreateImgFromInterval(
		Interval in)
	(ImgFactory out) =
	net.imagej.ops.create.imgFactory.DefaultCreateImgFactory(
		Dimensions dims?)
	(ImgLabeling out) =
	net.imagej.ops.create.imgLabeling.DefaultCreateImgLabeling(
		Dimensions in,
		IntegerType outType?,
		ImgFactory fac?,
		int maxNumLabelSets?)
	(ImgPlus out) =
	net.imagej.ops.create.imgPlus.DefaultCreateImgPlus(
		Img in,
		ImgPlusMetadata metadata?)
	(IntegerType out) =
	net.imagej.ops.create.integerType.DefaultCreateIntegerType(
		long maxValue?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernel.CreateKernel2D(
		double[][] in,
		ComplexType type?)
	(Img out) =
	net.imagej.ops.create.kernelDiffraction.DefaultCreateKernelGibsonLanni(
		Dimensions in,
		double NA,
		double lambda,
		double ns,
		double ni,
		double resLateral,
		double resAxial,
		double pZ,
		ComplexType type)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGauss.CreateKernelGaussDoubleType(
		double[] in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGauss.CreateKernelGaussSymmetric(
		Double in,
		int numDims,
		ComplexType type)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGauss.CreateKernelGaussSymmetricDoubleType(
		Double in,
		int numDims)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGauss.DefaultCreateKernelGauss(
		double[] in,
		ComplexType type)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelLog.CreateKernelLogDoubleType(
		double[] in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelLog.CreateKernelLogSymmetric(
		Double in,
		int numDims,
		ComplexType type)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelLog.CreateKernelLogSymmetricDoubleType(
		Double in,
		int numDims)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelLog.DefaultCreateKernelLog(
		double[] in,
		ComplexType type)
	(LabelingMapping out) =
	net.imagej.ops.create.labelingMapping.DefaultCreateLabelingMapping(
		int maxNumSets?)
	(NativeType out) =
	net.imagej.ops.create.nativeType.CreateNativeTypeFromClass(
		Class in)
	(DoubleType out) =
	net.imagej.ops.create.nativeType.DefaultCreateNativeType()
	(Object out) =
	net.imagej.ops.create.object.CreateObjectFromClass(
		Class in)
	(RandomAccessibleInterval arg) =
	net.imagej.ops.deconvolve.accelerate.VectorAccelerator(
		RandomAccessibleInterval arg)
	(Object out) =
	net.imagej.ops.eval.DefaultEval(
		String in,
		Map vars?)
	(DoubleType out?) =
	net.imagej.ops.features.haralick.DefaultASM(
		DoubleType out?,
		IterableInterval in,
		int numGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(double[] out) =
	net.imagej.ops.features.haralick.helper.CoocHXY(
		double[][] in)
	(DoubleType out) =
	net.imagej.ops.features.haralick.helper.CoocMeanX(
		double[][] in)
	(DoubleType out) =
	net.imagej.ops.features.haralick.helper.CoocMeanY(
		double[][] in)
	(double[] out) =
	net.imagej.ops.features.haralick.helper.CoocPX(
		double[][] in)
	(double[] out) =
	net.imagej.ops.features.haralick.helper.CoocPXMinusY(
		double[][] in)
	(double[] out) =
	net.imagej.ops.features.haralick.helper.CoocPXPlusY(
		double[][] in)
	(double[] out) =
	net.imagej.ops.features.haralick.helper.CoocPY(
		double[][] in)
	(DoubleType out) =
	net.imagej.ops.features.haralick.helper.CoocStdX(
		double[][] in)
	(DoubleType out) =
	net.imagej.ops.features.haralick.helper.CoocStdY(
		double[][] in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.features.hog.HistogramOfOrientedGradients2D(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		int numOrientations,
		int spanOfNeighborhood)
	(ZernikeMoment out) =
	net.imagej.ops.features.zernike.helper.ZernikeComputer(
		IterableInterval in,
		int order,
		int repetition)
	(RealType out) =
	net.imagej.ops.filter.addNoise.AddNoiseRealType(
		RealType out,
		RealType in,
		double rangeMin,
		double rangeMax,
		double rangeStdDev,
		long seed?)
	(RealType out) =
	net.imagej.ops.filter.addPoissonNoise.AddPoissonNoiseRealType(
		RealType out,
		RealType in,
		long seed?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.bilateral.DefaultBilateral(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in,
		double sigmaR,
		double sigmaS,
		int radius)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.convolve.ConvolveNaiveC(
		RandomAccessibleInterval out,
		RandomAccessible in,
		RandomAccessibleInterval kernel)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.convolve.PadAndConvolveFFT(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		long[] borderSize?,
		OutOfBoundsFactory obfInput?,
		OutOfBoundsFactory obfKernel?,
		RealType outType?,
		ComplexType fftType?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.correlate.CorrelateFFTC(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		RandomAccessibleInterval fftInput?,
		RandomAccessibleInterval fftKernel?,
		boolean performInputFFT?,
		boolean performKernelFFT?)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.filter.derivative.PartialDerivativeRAI(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		int dimension)
	(CompositeIntervalView out) =
	net.imagej.ops.filter.derivative.PartialDerivativesRAI(
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.derivativeGauss.DefaultDerivativeGauss(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		int[] in2,
		double[] sigma)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.filter.dog.DefaultDoG(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		UnaryComputerOp gauss1,
		UnaryComputerOp gauss2,
		UnaryFunctionOp outputCreator,
		UnaryFunctionOp tmpCreator)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.filter.dog.DoGVaryingSigmas(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		double[] sigmas1,
		double[] sigmas2,
		OutOfBoundsFactory fac?)
	(Img out) =
	net.imagej.ops.filter.fft.CreateOutputFFTMethods(
		Dimensions in1,
		Object in2,
		boolean fast?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.fft.FFTMethodsOpC(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in)
	(long[][] out) =
	net.imagej.ops.filter.fftSize.ComputeFFTMethodsSize(
		Dimensions in,
		boolean forward,
		boolean fast)
	(long[][] out) =
	net.imagej.ops.filter.fftSize.DefaultComputeFFTSize(
		Dimensions in,
		boolean powerOfTwo)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.findEdges.DefaultFindEdges(
		RandomAccessibleInterval in)
	(CompositeIntervalView out) =
	net.imagej.ops.filter.hessian.HessianRAI(
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.ifft.IFFTMethodsOpC(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval arg) =
	net.imagej.ops.filter.ifft.IFFTMethodsOpI(
		RandomAccessibleInterval arg)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.pad.DefaultPadInputFFT(
		RandomAccessibleInterval in1,
		Dimensions in2,
		boolean fast?,
		OutOfBoundsFactory obf?)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.filter.sobel.SobelRAI(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(IterableInterval out?) =
	net.imagej.ops.filter.tubeness.DefaultTubeness(
		IterableInterval out?,
		RandomAccessibleInterval in,
		double sigma,
		double[] calibration)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.vesselness.DefaultFrangi(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in,
		double[] spacing,
		int scale)
	(RealLocalizable out) =
	net.imagej.ops.geom.DefaultCenterOfGravity(
		IterableInterval in)
	(Polygon2D out) =
	net.imagej.ops.geom.geom2d.DefaultBoundingBox(
		Polygon2D in)
	(Polygon2D out) =
	net.imagej.ops.geom.geom2d.DefaultContour(
		RandomAccessibleInterval in,
		boolean useJacobs)
	(Polygon2D out) =
	net.imagej.ops.geom.geom2d.DefaultConvexHull2D(
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultFeretsDiameterForAngle(
		DoubleType out?,
		Polygon2D in,
		double angle)
	(Pair out) =
	net.imagej.ops.geom.geom2d.DefaultMaximumFeret(
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultMaximumFeretAngle(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultMaximumFeretDiameter(
		DoubleType out?,
		Polygon2D in)
	(Pair out) =
	net.imagej.ops.geom.geom2d.DefaultMinimumFeret(
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultMinimumFeretAngle(
		DoubleType out?,
		Polygon2D in)
	(DoubleType out?) =
	net.imagej.ops.geom.geom2d.DefaultMinimumFeretDiameter(
		DoubleType out?,
		Polygon2D in)
	(Pair out) =
	net.imagej.ops.geom.geom2d.DefaultMinorMajorAxis(
		Polygon2D in)
	(Mesh out,
		double epsilon) =
	net.imagej.ops.geom.geom3d.DefaultConvexHull3D(
		Mesh in)
	(RealMatrix out) =
	net.imagej.ops.geom.geom3d.DefaultInertiaTensor3D(
		IterableRegion in)
	(RealMatrix out) =
	net.imagej.ops.geom.geom3d.DefaultInertiaTensor3DMesh(
		Mesh in)
	(Mesh out) =
	net.imagej.ops.geom.geom3d.DefaultMarchingCubes(
		RandomAccessibleInterval in,
		double isolevel?,
		VertexInterpolator interpolatorClass?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.geom.geom3d.DefaultVoxelization3D(
		Mesh in,
		int width?,
		int height?,
		int depth?)
	(double[] output) =
	net.imagej.ops.geom.geom3d.mesh.BitTypeVertexInterpolator(
		int[] p1,
		int[] p2,
		double p1Value,
		double p2Value)
	(double[] output) =
	net.imagej.ops.geom.geom3d.mesh.DefaultVertexInterpolator(
		int[] p1,
		int[] p2,
		double p1Value,
		double p2Value,
		double isolevel)
	(String help) =
	net.imagej.ops.help.HelpCandidates(
		String name?,
		Class opType?,
		Integer arity?,
		Flavor flavor?)
	(Object arg) =
	net.imagej.ops.identity.DefaultIdentity(
		Object arg)
	(String out) =
	net.imagej.ops.image.ascii.DefaultASCII(
		IterableInterval in,
		RealType min?,
		RealType max?)
	(double[][] out) =
	net.imagej.ops.image.cooccurrenceMatrix.CooccurrenceMatrix2D(
		IterableInterval in,
		int nrGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(double[][] out) =
	net.imagej.ops.image.cooccurrenceMatrix.CooccurrenceMatrix3D(
		IterableInterval in,
		int nrGreyLevels,
		int distance,
		MatrixOrientation orientation)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.distancetransform.DistanceTransform2D(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.distancetransform.DistanceTransform2DCalibration(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		double[] calibration)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.distancetransform.DistanceTransform3D(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.distancetransform.DistanceTransform3DCalibration(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		double[] calibration)
	(IterableInterval out) =
	net.imagej.ops.image.equation.DefaultCoordinatesEquation(
		IterableInterval out,
		UnaryFunctionOp in)
	(IterableInterval out?) =
	net.imagej.ops.image.equation.DefaultEquation(
		IterableInterval out?,
		String in)
	(IterableInterval out) =
	net.imagej.ops.image.equation.DefaultXYEquation(
		IterableInterval out,
		DoubleBinaryOperator in)
	(Iterable out) =
	net.imagej.ops.image.fill.DefaultFill(
		Iterable out,
		Type constant)
	(Histogram1d out) =
	net.imagej.ops.image.histogram.HistogramCreate(
		Iterable in,
		int numBins?)
	(IterableInterval out) =
	net.imagej.ops.image.invert.InvertII(
		IterableInterval out,
		IterableInterval in,
		RealType min?,
		RealType max?)
	(IterableInterval out) =
	net.imagej.ops.image.normalize.NormalizeIIComputer(
		IterableInterval out,
		IterableInterval in,
		RealType sourceMin?,
		RealType sourceMax?,
		RealType targetMin?,
		RealType targetMax?)
	(IterableInterval out) =
	net.imagej.ops.image.normalize.NormalizeIIFunction(
		IterableInterval in,
		RealType sourceMin?,
		RealType sourceMax?,
		RealType targetMin?,
		RealType targetMax?,
		boolean isLazy?)
	(ImgLabeling out?) =
	net.imagej.ops.image.watershed.Watershed(
		ImgLabeling out?,
		RandomAccessibleInterval in,
		boolean useEightConnectivity,
		boolean drawWatersheds,
		RandomAccessibleInterval mask?)
	(ImgLabeling out?) =
	net.imagej.ops.image.watershed.WatershedBinary(
		ImgLabeling out?,
		RandomAccessibleInterval in,
		boolean useEightConnectivity,
		boolean drawWatersheds,
		double[] sigma,
		RandomAccessibleInterval mask?)
	(ImgLabeling out?) =
	net.imagej.ops.image.watershed.WatershedBinarySingleSigma(
		ImgLabeling out?,
		RandomAccessibleInterval in,
		boolean useEightConnectivity,
		boolean drawWatersheds,
		double sigma,
		RandomAccessibleInterval mask?)
	(ImgLabeling out?) =
	net.imagej.ops.image.watershed.WatershedSeeded(
		ImgLabeling out?,
		RandomAccessibleInterval in,
		ImgLabeling seeds,
		boolean useEightConnectivity,
		boolean drawWatersheds,
		RandomAccessibleInterval mask?)
	(Object out) =
	net.imagej.ops.join.DefaultJoin2Computers(
		Object out,
		Object in,
		UnaryComputerOp first,
		UnaryComputerOp second,
		UnaryOutputFactory bufferFactory)
	(Object arg) =
	net.imagej.ops.join.DefaultJoin2Inplaces(
		Object arg,
		UnaryInplaceOp first,
		UnaryInplaceOp second)
	(Object out) =
	net.imagej.ops.join.DefaultJoinComputerAndInplace(
		Object out,
		Object in,
		UnaryComputerOp first,
		UnaryInplaceOp second)
	(Object out) =
	net.imagej.ops.join.DefaultJoinInplaceAndComputer(
		Object out,
		Object in,
		UnaryInplaceOp first,
		UnaryComputerOp second)
	(Object out) =
	net.imagej.ops.join.DefaultJoinNComputers(
		Object out,
		Object in,
		List ops,
		UnaryOutputFactory outputFactory)
	(Object arg) =
	net.imagej.ops.join.DefaultJoinNInplaces(
		Object arg,
		List ops)
	(Vector3d out?) =
	net.imagej.ops.linalg.rotate.Rotate3d(
		Vector3d out?,
		Vector3d in1,
		Quaterniondc in2)
	(Vector3f out?) =
	net.imagej.ops.linalg.rotate.Rotate3f(
		Vector3f out?,
		Vector3f in1,
		Quaternionfc in2)
	(BooleanType out?) =
	net.imagej.ops.logic.BooleanTypeLogic$And(
		BooleanType out?,
		BooleanType in1,
		BooleanType in2)
	(BooleanType out) =
	net.imagej.ops.logic.BooleanTypeLogic$ComparableGreaterThan(
		BooleanType out,
		Comparable in1,
		Comparable in2)
	(BooleanType out) =
	net.imagej.ops.logic.BooleanTypeLogic$ComparableGreaterThanOrEqual(
		BooleanType out,
		Comparable in1,
		Comparable in2)
	(BooleanType out) =
	net.imagej.ops.logic.BooleanTypeLogic$ComparableLessThan(
		BooleanType out,
		Comparable in1,
		Comparable in2)
	(BooleanType out) =
	net.imagej.ops.logic.BooleanTypeLogic$ComparableLessThanOrEqual(
		BooleanType out,
		Comparable in1,
		Comparable in2)
	(BooleanType out?) =
	net.imagej.ops.logic.BooleanTypeLogic$Not(
		BooleanType out?,
		BooleanType in)
	(BooleanType out) =
	net.imagej.ops.logic.BooleanTypeLogic$ObjectsEqual(
		BooleanType out,
		Object in1,
		Object in2)
	(BooleanType out) =
	net.imagej.ops.logic.BooleanTypeLogic$ObjectsNotEqual(
		BooleanType out,
		Object in1,
		Object in2)
	(BooleanType out?) =
	net.imagej.ops.logic.BooleanTypeLogic$Or(
		BooleanType out?,
		BooleanType in1,
		BooleanType in2)
	(BooleanType out?) =
	net.imagej.ops.logic.BooleanTypeLogic$Xor(
		BooleanType out?,
		BooleanType in1,
		BooleanType in2)
	(Type out) =
	net.imagej.ops.logic.Default(
		Type out,
		BooleanType in,
		Type defaultVal)
	(IterableInterval out?) =
	net.imagej.ops.logic.IIToIIOutputII$And(
		IterableInterval out?,
		IterableInterval in1,
		IterableInterval in2)
	(IterableInterval out?) =
	net.imagej.ops.logic.IIToIIOutputII$Or(
		IterableInterval out?,
		IterableInterval in1,
		IterableInterval in2)
	(IterableInterval out?) =
	net.imagej.ops.logic.IIToIIOutputII$Xor(
		IterableInterval out?,
		IterableInterval in1,
		IterableInterval in2)
	(IterableInterval out?) =
	net.imagej.ops.logic.IIToRAIOutputII$And(
		IterableInterval out?,
		IterableInterval in1,
		RandomAccessibleInterval in2)
	(IterableInterval out?) =
	net.imagej.ops.logic.IIToRAIOutputII$Or(
		IterableInterval out?,
		IterableInterval in1,
		RandomAccessibleInterval in2)
	(IterableInterval out?) =
	net.imagej.ops.logic.IIToRAIOutputII$Xor(
		IterableInterval out?,
		IterableInterval in1,
		RandomAccessibleInterval in2)
	(Type out?) =
	net.imagej.ops.logic.If(
		Type out?,
		BooleanType in,
		Type ifTrueVal,
		Type ifFalseVal)
	(Op out) =
	net.imagej.ops.lookup.LookupByName(
		String in,
		Object[] args)
	(Op out) =
	net.imagej.ops.lookup.LookupByType(
		Class in,
		Object[] args)
	(Object out) =
	net.imagej.ops.loop.DefaultLoopComputer(
		Object out,
		Object in,
		UnaryComputerOp op,
		UnaryOutputFactory outputFactory,
		int n)
	(Object arg) =
	net.imagej.ops.loop.DefaultLoopInplace(
		Object arg,
		UnaryInplaceOp op,
		int n)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapViewRAIToRAI(
		RandomAccessibleInterval in,
		UnaryComputerOp op,
		Type type)
	(RandomAccessible out) =
	net.imagej.ops.map.MapViewRandomAccessToRandomAccess(
		RandomAccessible in,
		UnaryComputerOp op,
		Type type)
	(RealType out) =
	net.imagej.ops.math.BinaryRealTypeMath$Add(
		RealType out,
		RealType in1,
		RealType in2)
	(RealType out) =
	net.imagej.ops.math.BinaryRealTypeMath$And(
		RealType out,
		RealType in1,
		RealType in2)
	(RealType out) =
	net.imagej.ops.math.BinaryRealTypeMath$Divide(
		RealType out,
		RealType in1,
		RealType in2,
		double dbzVal)
	(RealType out) =
	net.imagej.ops.math.BinaryRealTypeMath$Multiply(
		RealType out,
		RealType in1,
		RealType in2)
	(RealType out) =
	net.imagej.ops.math.BinaryRealTypeMath$Or(
		RealType out,
		RealType in1,
		RealType in2)
	(RealType out) =
	net.imagej.ops.math.BinaryRealTypeMath$Subtract(
		RealType out,
		RealType in1,
		RealType in2)
	(RealType out) =
	net.imagej.ops.math.BinaryRealTypeMath$Xor(
		RealType out,
		RealType in1,
		RealType in2)
	(IterableInterval out?) =
	net.imagej.ops.math.ConstantToIIOutputII$Add(
		IterableInterval out?,
		IterableInterval in,
		NumericType value)
	(IterableInterval out?) =
	net.imagej.ops.math.ConstantToIIOutputII$Divide(
		IterableInterval out?,
		IterableInterval in,
		NumericType value)
	(IterableInterval out?) =
	net.imagej.ops.math.ConstantToIIOutputII$Multiply(
		IterableInterval out?,
		IterableInterval in,
		NumericType value)
	(IterableInterval out?) =
	net.imagej.ops.math.ConstantToIIOutputII$Subtract(
		IterableInterval out?,
		IterableInterval in,
		NumericType value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$AddByte(
		PlanarImg arg,
		byte value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$AddDouble(
		PlanarImg arg,
		double value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$AddFloat(
		PlanarImg arg,
		float value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$AddInt(
		PlanarImg arg,
		int value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$AddLong(
		PlanarImg arg,
		long value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$AddShort(
		PlanarImg arg,
		short value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$AddUnsignedByte(
		PlanarImg arg,
		byte value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$AddUnsignedInt(
		PlanarImg arg,
		int value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$AddUnsignedLong(
		PlanarImg arg,
		long value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$AddUnsignedShort(
		PlanarImg arg,
		short value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$DivideByte(
		PlanarImg arg,
		byte value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$DivideDouble(
		PlanarImg arg,
		double value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$DivideFloat(
		PlanarImg arg,
		float value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$DivideInt(
		PlanarImg arg,
		int value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$DivideLong(
		PlanarImg arg,
		long value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$DivideShort(
		PlanarImg arg,
		short value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$DivideUnsignedByte(
		PlanarImg arg,
		byte value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$DivideUnsignedInt(
		PlanarImg arg,
		int value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$DivideUnsignedLong(
		PlanarImg arg,
		long value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$DivideUnsignedShort(
		PlanarImg arg,
		short value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$MultiplyByte(
		PlanarImg arg,
		byte value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$MultiplyDouble(
		PlanarImg arg,
		double value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$MultiplyFloat(
		PlanarImg arg,
		float value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$MultiplyInt(
		PlanarImg arg,
		int value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$MultiplyLong(
		PlanarImg arg,
		long value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$MultiplyShort(
		PlanarImg arg,
		short value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$MultiplyUnsignedByte(
		PlanarImg arg,
		byte value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$MultiplyUnsignedInt(
		PlanarImg arg,
		int value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$MultiplyUnsignedLong(
		PlanarImg arg,
		long value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$MultiplyUnsignedShort(
		PlanarImg arg,
		short value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$SubtractByte(
		PlanarImg arg,
		byte value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$SubtractDouble(
		PlanarImg arg,
		double value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$SubtractFloat(
		PlanarImg arg,
		float value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$SubtractInt(
		PlanarImg arg,
		int value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$SubtractLong(
		PlanarImg arg,
		long value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$SubtractShort(
		PlanarImg arg,
		short value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$SubtractUnsignedByte(
		PlanarImg arg,
		byte value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$SubtractUnsignedInt(
		PlanarImg arg,
		int value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$SubtractUnsignedLong(
		PlanarImg arg,
		long value)
	(PlanarImg arg) =
	net.imagej.ops.math.ConstantToPlanarImage$SubtractUnsignedShort(
		PlanarImg arg,
		short value)
	(IterableInterval out?) =
	net.imagej.ops.math.IIToRAIOutputII$Add(
		IterableInterval out?,
		IterableInterval in1,
		RandomAccessibleInterval in2)
	(IterableInterval out?) =
	net.imagej.ops.math.IIToRAIOutputII$Divide(
		IterableInterval out?,
		IterableInterval in1,
		RandomAccessibleInterval in2)
	(IterableInterval out?) =
	net.imagej.ops.math.IIToRAIOutputII$Multiply(
		IterableInterval out?,
		IterableInterval in1,
		RandomAccessibleInterval in2)
	(IterableInterval out?) =
	net.imagej.ops.math.IIToRAIOutputII$Subtract(
		IterableInterval out?,
		IterableInterval in1,
		RandomAccessibleInterval in2)
	(Type out) =
	net.imagej.ops.math.NullaryNumericTypeMath$Assign(
		Type out,
		Type constant)
	(NumericType out) =
	net.imagej.ops.math.NullaryNumericTypeMath$Zero(
		NumericType out)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Abs(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arccos(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arccosh(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arccot(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arccoth(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arccsc(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arccsch(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arcsec(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arcsech(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arcsin(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arcsinh(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arctan(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Arctanh(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Ceil(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Cos(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Cosh(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Cot(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Coth(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Csc(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Csch(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$CubeRoot(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Exp(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$ExpMinusOne(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Floor(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$GammaConstant(
		RealType out,
		RealType in,
		double constant)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Invert(
		RealType out,
		RealType in,
		double specifiedMin,
		double specifiedMax)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Log(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Log10(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Log2(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$LogOnePlusX(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$MaxConstant(
		RealType out,
		RealType in,
		double constant)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$MinConstant(
		RealType out,
		RealType in,
		double constant)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$NearestInt(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Negate(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$PowerConstant(
		RealType out,
		RealType in,
		double constant)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$RandomGaussian(
		RealType out,
		RealType in,
		long seed?)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$RandomUniform(
		RealType out,
		RealType in,
		long seed?)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Reciprocal(
		RealType out,
		RealType in,
		double dbzVal)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Round(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Sec(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Sech(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Signum(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Sin(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Sinc(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$SincPi(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Sinh(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Sqr(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Sqrt(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Step(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Tan(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Tanh(
		RealType out,
		RealType in)
	(RealType out) =
	net.imagej.ops.math.UnaryRealTypeMath$Ulp(
		RealType out,
		RealType in)
	(IterableInterval out?) =
	net.imagej.ops.morphology.blackTopHat.ListBlackTopHat(
		IterableInterval out?,
		RandomAccessibleInterval in1,
		List in2)
	(IterableInterval out?) =
	net.imagej.ops.morphology.close.ListClose(
		IterableInterval out?,
		RandomAccessibleInterval in1,
		List in2)
	(IterableInterval out?) =
	net.imagej.ops.morphology.dilate.DefaultDilate(
		IterableInterval out?,
		RandomAccessibleInterval in1,
		Shape in2,
		boolean isFull?,
		OutOfBoundsFactory f?)
	(IterableInterval out?) =
	net.imagej.ops.morphology.erode.DefaultErode(
		IterableInterval out?,
		RandomAccessibleInterval in1,
		Shape in2,
		boolean isFull?,
		OutOfBoundsFactory f?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.morphology.extractHoles.DefaultExtractHolesComputer(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in,
		Shape structElement?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.morphology.extractHoles.DefaultExtractHolesFunction(
		RandomAccessibleInterval in,
		Shape structElement?)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.morphology.fillHoles.DefaultFillHoles(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		Shape structElement?)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.morphology.floodFill.DefaultFloodFill(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in1,
		Localizable in2,
		Shape structElement)
	(IterableInterval out?) =
	net.imagej.ops.morphology.open.ListOpen(
		IterableInterval out?,
		RandomAccessibleInterval in1,
		List in2)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.morphology.outline.Outline(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in1,
		Boolean in2)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.morphology.thin.ThinGuoHall(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.morphology.thin.ThinHilditch(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.morphology.thin.ThinMorphological(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.morphology.thin.ThinZhangSuen(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(IterableInterval out?) =
	net.imagej.ops.morphology.topHat.ListTopHat(
		IterableInterval out?,
		RandomAccessibleInterval in1,
		List in2)
	(Object out) =
	net.imagej.ops.run.RunByName(
		String in,
		Object[] args)
	(Object out) =
	net.imagej.ops.run.RunByOp(
		Op in,
		Object[] args)
	(Object out) =
	net.imagej.ops.run.RunByType(
		Class in,
		Object[] args)
	(List out) =
	net.imagej.ops.segment.detectJunctions.DefaultDetectJunctions(
		List in,
		double threshold?)
	(List out) =
	net.imagej.ops.segment.detectRidges.DefaultDetectRidges(
		RandomAccessibleInterval in,
		double width,
		double lowerThreshold,
		double higherThreshold,
		int ridgeLengthMin)
	(DoubleType out) =
	net.imagej.ops.stats.IntegralMean(
		DoubleType out,
		RectangleNeighborhood in)
	(DoubleType out?) =
	net.imagej.ops.stats.IntegralSum(
		DoubleType out?,
		RectangleNeighborhood in)
	(DoubleType out) =
	net.imagej.ops.stats.IntegralVariance(
		DoubleType out,
		RectangleNeighborhood in)
	(Matrix4d out) =
	net.imagej.ops.stats.regression.leastSquares.Quadric(
		Collection in)
	net.imagej.ops.thread.chunker.DefaultChunker(
		Chunk chunkable,
		long numberOfElements)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Huang(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$IJ1(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Intermodes(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$IsoData(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Li(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$MaxEntropy(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$MaxLikelihood(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Mean(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$MinError(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Minimum(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Moments(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Otsu(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Percentile(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$RenyiEntropy(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Rosin(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Shanbhag(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Triangle(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out?) =
	net.imagej.ops.threshold.ApplyThresholdMethod$Yen(
		IterableInterval out?,
		IterableInterval in)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalHuangThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalIJ1Threshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalIntermodesThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalIsoDataThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalLiThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalMaxEntropyThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalMaxLikelihoodThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalMinErrorThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalMinimumThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalMomentsThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalOtsuThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalPercentileThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalRenyiEntropyThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalRosinThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalShanbhagThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalTriangleThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.ApplyThresholdMethodLocal$LocalYenThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out?) =
	net.imagej.ops.threshold.apply.ApplyManualThreshold(
		IterableInterval out?,
		IterableInterval in,
		RealType threshold)
	(BitType out) =
	net.imagej.ops.threshold.apply.ApplyThresholdComparable(
		BitType out,
		Comparable in1,
		Object in2)
	(BitType out) =
	net.imagej.ops.threshold.apply.ApplyThresholdComparator(
		BitType out,
		Object in1,
		Object in2,
		Comparator comparator)
	(IterableInterval out) =
	net.imagej.ops.threshold.localBernsen.LocalBernsenThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double contrastThreshold,
		double halfMaxValue)
	(IterableInterval out) =
	net.imagej.ops.threshold.localContrast.LocalContrastThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.threshold.localMedian.LocalMedianThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c)
	(IterableInterval out) =
	net.imagej.ops.threshold.localMidGrey.LocalMidGreyThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c)
	(List out) =
	net.imagej.ops.topology.BoxCount(
		RandomAccessibleInterval in,
		Long maxSize?,
		Long minSize?,
		Double scaling?,
		Long gridMoves?)
	(DoubleType out?) =
	net.imagej.ops.topology.eulerCharacteristic.EulerCharacteristic26N(
		DoubleType out?,
		RandomAccessibleInterval in)
	(DoubleType out?) =
	net.imagej.ops.topology.eulerCharacteristic.EulerCharacteristic26NFloating(
		DoubleType out?,
		RandomAccessibleInterval in)
	(DoubleType out?) =
	net.imagej.ops.topology.eulerCharacteristic.EulerCorrection(
		DoubleType out?,
		RandomAccessibleInterval in)
	(CompositeIntervalView out) =
	net.imagej.ops.transform.collapseNumericView.DefaultCollapseNumeric2CompositeIntervalView(
		RandomAccessibleInterval in)
	(CompositeView out) =
	net.imagej.ops.transform.collapseNumericView.DefaultCollapseNumeric2CompositeView(
		RandomAccessible in,
		int numChannels)
	(CompositeIntervalView out) =
	net.imagej.ops.transform.collapseRealView.DefaultCollapseReal2CompositeIntervalView(
		RandomAccessibleInterval in)
	(CompositeView out) =
	net.imagej.ops.transform.collapseRealView.DefaultCollapseReal2CompositeView(
		RandomAccessible in,
		int numChannels)
	(CompositeIntervalView out) =
	net.imagej.ops.transform.collapseView.DefaultCollapse2CompositeIntervalView(
		RandomAccessibleInterval in)
	(CompositeView out) =
	net.imagej.ops.transform.collapseView.DefaultCollapse2CompositeView(
		RandomAccessible in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.concatenateView.ConcatenateViewWithAccessMode(
		List in,
		int concatenationAxis,
		StackAccessMode stackAccessMode)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.concatenateView.DefaultConcatenateView(
		List in,
		int concatenationAxis)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.dropSingletonDimensionsView.DefaultDropSingletonDimensionsView(
		RandomAccessibleInterval in)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendBorderView.DefaultExtendBorderView(
		RandomAccessibleInterval in)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendMirrorDoubleView.DefaultExtendMirrorDoubleView(
		RandomAccessibleInterval in)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendMirrorSingleView.DefaultExtendMirrorSingleView(
		RandomAccessibleInterval in)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendPeriodicView.DefaultExtendPeriodicView(
		RandomAccessibleInterval in)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendRandomView.DefaultExtendRandomView(
		RandomAccessibleInterval in,
		double min,
		double max)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendValueView.DefaultExtendValueView(
		RandomAccessibleInterval in,
		Type value)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendView.DefaultExtendView(
		RandomAccessibleInterval in,
		OutOfBoundsFactory factory)
	(ExtendedRandomAccessibleInterval out) =
	net.imagej.ops.transform.extendZeroView.DefaultExtendZeroView(
		RandomAccessibleInterval in)
	(IterableInterval out) =
	net.imagej.ops.transform.flatIterableView.DefaultFlatIterableView(
		RandomAccessibleInterval in)
	(MixedTransformView out) =
	net.imagej.ops.transform.hyperSliceView.DefaultHyperSliceView(
		RandomAccessible in,
		int d,
		long pos)
	(RealRandomAccessible out) =
	net.imagej.ops.transform.interpolateView.DefaultInterpolateView(
		EuclideanSpace in,
		InterpolatorFactory factory)
	(IntervalView out) =
	net.imagej.ops.transform.intervalView.DefaultIntervalView(
		RandomAccessible in,
		Interval interval)
	(IntervalView out) =
	net.imagej.ops.transform.intervalView.IntervalViewMinMax(
		RandomAccessible in,
		long[] min,
		long[] max)
	(MixedTransformView out) =
	net.imagej.ops.transform.invertAxisView.DefaultInvertAxisView(
		RandomAccessible in,
		int d)
	(MixedTransformView out) =
	net.imagej.ops.transform.offsetView.DefaultOffsetView(
		RandomAccessible in,
		long[] offset)
	(IntervalView out) =
	net.imagej.ops.transform.offsetView.OffsetViewInterval(
		RandomAccessible in,
		Interval interval)
	(IntervalView out) =
	net.imagej.ops.transform.offsetView.OffsetViewOriginSize(
		RandomAccessible in,
		long[] origin,
		long[] dimension)
	(IntervalView out) =
	net.imagej.ops.transform.permuteCoordinatesInverseView.DefaultPermuteCoordinatesInverseView(
		RandomAccessibleInterval in,
		int[] permutation)
	(IntervalView out) =
	net.imagej.ops.transform.permuteCoordinatesInverseView.PermuteCoordinateInverseViewOfDimension(
		RandomAccessibleInterval in,
		int[] permutation,
		int d)
	(IntervalView out) =
	net.imagej.ops.transform.permuteCoordinatesView.DefaultPermuteCoordinatesView(
		RandomAccessibleInterval in,
		int[] permutation)
	(IntervalView out) =
	net.imagej.ops.transform.permuteCoordinatesView.PermuteCoordinatesViewOfDimension(
		RandomAccessibleInterval in,
		int[] permutation,
		int d)
	(MixedTransformView out) =
	net.imagej.ops.transform.permuteView.DefaultPermuteView(
		RandomAccessible in,
		int fromAxis,
		int toAxis)
	(RandomAccessibleOnRealRandomAccessible out) =
	net.imagej.ops.transform.rasterView.DefaultRasterView(
		RealRandomAccessible in)
	(MixedTransformView out) =
	net.imagej.ops.transform.rotateView.DefaultRotateView(
		RandomAccessible in,
		int fromAxis,
		int toAxis)
	(TransformView out) =
	net.imagej.ops.transform.shearView.DefaultShearView(
		RandomAccessible in,
		int shearDimension,
		int referenceDimension)
	(IntervalView out) =
	net.imagej.ops.transform.shearView.ShearViewInterval(
		RandomAccessible in,
		Interval interval,
		int shearDimension,
		int referenceDimension)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.stackView.DefaultStackView(
		List in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.stackView.StackViewWithAccessMode(
		List in,
		StackAccessMode stackAccessMode)
	(SubsampleView out) =
	net.imagej.ops.transform.subsampleView.DefaultSubsampleView(
		RandomAccessible in,
		long step)
	(SubsampleView out) =
	net.imagej.ops.transform.subsampleView.SubsampleViewStepsForDims(
		RandomAccessible in,
		long[] steps)
	(MixedTransformView out) =
	net.imagej.ops.transform.translateView.DefaultTranslateView(
		RandomAccessible in,
		long[] translation)
	(TransformView out) =
	net.imagej.ops.transform.unshearView.DefaultUnshearView(
		RandomAccessible in,
		int shearDimension,
		int referenceDimension)
	(IntervalView out) =
	net.imagej.ops.transform.unshearView.UnshearViewInterval(
		RandomAccessible in,
		Interval interval,
		int shearDimension,
		int referenceDimension)
	(IntervalView out) =
	net.imagej.ops.transform.zeroMinView.DefaultZeroMinView(
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.structure.SingleStructureTensorEigenvaluesFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double sigma,
		double integrationScale)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.structure.StructureTensorEigenvaluesFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.stats.SingleVarianceFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings,
		double radius)
	(RandomAccessibleInterval out) =
	sc.fiji.labkit.pixel_classification.pixel_feature.filter.stats.VarianceFeature(
		RandomAccessibleInterval in,
		GlobalSettings globalSettings)
	(BitType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToBit(
		BitType out?,
		ComplexType in)
	(ComplexFloatType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToCfloat32(
		ComplexFloatType out?,
		ComplexType in)
	(ComplexDoubleType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToCfloat64(
		ComplexDoubleType out?,
		ComplexType in)
	(FloatType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToFloat32(
		FloatType out?,
		ComplexType in)
	(DoubleType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToFloat64(
		DoubleType out?,
		ComplexType in)
	(ShortType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToInt16(
		ShortType out?,
		ComplexType in)
	(IntType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToInt32(
		IntType out?,
		ComplexType in)
	(LongType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToInt64(
		LongType out?,
		ComplexType in)
	(ByteType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToInt8(
		ByteType out?,
		ComplexType in)
	(Unsigned12BitType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint12(
		Unsigned12BitType out?,
		ComplexType in)
	(Unsigned128BitType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint128(
		Unsigned128BitType out?,
		ComplexType in)
	(UnsignedShortType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint16(
		UnsignedShortType out?,
		ComplexType in)
	(Unsigned2BitType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint2(
		Unsigned2BitType out?,
		ComplexType in)
	(UnsignedIntType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint32(
		UnsignedIntType out?,
		ComplexType in)
	(Unsigned4BitType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint4(
		Unsigned4BitType out?,
		ComplexType in)
	(UnsignedLongType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint64(
		UnsignedLongType out?,
		ComplexType in)
	(UnsignedByteType out?) =
	net.imagej.ops.convert.ConvertTypes$ComplexToUint8(
		UnsignedByteType out?,
		ComplexType in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelBiGauss.CreateKernel2ndDerivBiGaussDoubleType(
		double[] in1,
		Integer in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelBiGauss.DefaultCreateKernel2ndDerivBiGauss(
		double[] in1,
		Integer in2,
		ComplexType typeVar)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelBiGauss.DefaultCreateKernelBiGauss(
		double[] in1,
		Integer in2,
		ComplexType typeVar)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelBiGauss.CreateKernelBiGaussDoubleType(
		double[] in1,
		Integer in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.DefaultCreateKernelGabor(
		double[] in1,
		double[] in2,
		ComplexType typeVar)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.CreateKernelGaborIsotropic(
		Double in1,
		double[] in2,
		ComplexType typeVar)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.CreateKernelGaborComplexDoubleType(
		double[] in1,
		double[] in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.CreateKernelGaborIsotropicComplexDoubleType(
		Double in1,
		double[] in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.CreateKernelGaborIsotropicDoubleType(
		Double in1,
		double[] in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelGabor.CreateKernelGaborDoubleType(
		double[] in1,
		double[] in2)
	(RandomAccessibleInterval out) =
	net.imagej.ops.create.kernelSobel.CreateKernelSobel(
		ComplexType type)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndIIToIIParallel(
		IterableInterval out,
		IterableInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndIIToRAIParallel(
		RandomAccessibleInterval out,
		IterableInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndRAIToIIParallel(
		IterableInterval out,
		IterableInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndRAIToRAIParallel(
		RandomAccessibleInterval out,
		IterableInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndIIToIIParallel(
		IterableInterval out,
		RandomAccessibleInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$IIAndIIParallel(
		IterableInterval arg,
		IterableInterval in,
		BinaryInplace1Op op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndIIToRAIParallel(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$IIAndRAIParallel(
		IterableInterval arg,
		RandomAccessibleInterval in,
		BinaryInplace1Op op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndRAIToIIParallel(
		IterableInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(RandomAccessibleInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$RAIAndIIParallel(
		RandomAccessibleInterval arg,
		IterableInterval in,
		BinaryInplace1Op op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapIIAndIIInplaceParallel(
		IterableInterval arg,
		IterableInterval in,
		BinaryInplaceOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndIIToII(
		IterableInterval out,
		IterableInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndIIToRAI(
		RandomAccessibleInterval out,
		IterableInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndRAIToII(
		IterableInterval out,
		IterableInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapIIInplaceParallel(
		IterableInterval arg,
		UnaryInplaceOp op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$IIAndRAIToRAI(
		RandomAccessibleInterval out,
		IterableInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndIIToII(
		IterableInterval out,
		RandomAccessibleInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$IIAndII(
		IterableInterval arg,
		IterableInterval in,
		BinaryInplace1Op op)
	(RandomAccessibleInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndIIToRAI(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		IterableInterval in2,
		BinaryComputerOp op)
	(IterableInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$IIAndRAI(
		IterableInterval arg,
		RandomAccessibleInterval in,
		BinaryInplace1Op op)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.integral.DefaultIntegralImg(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.integral.SquareIntegralImg(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(IterableInterval out) =
	net.imagej.ops.map.MapBinaryComputers$RAIAndRAIToII(
		IterableInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		BinaryComputerOp op)
	(RandomAccessibleInterval arg) =
	net.imagej.ops.map.MapBinaryInplace1s$RAIAndII(
		RandomAccessibleInterval arg,
		IterableInterval in,
		BinaryInplace1Op op)
	(IterableInterval out) =
	net.imagej.ops.map.MapNullaryII(
		IterableInterval out,
		NullaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.neighborhood.MapNeighborhoodWithCenter(
		IterableInterval out,
		RandomAccessibleInterval in1,
		Shape in2,
		CenterAwareComputerOp op)
	(ImgPlus out) =
	net.imagej.ops.transform.crop.CropImgPlus(
		ImgPlus in1,
		Interval in2,
		boolean dropSingleDimensions?)
	(IterableInterval out) =
	net.imagej.ops.transform.project.DefaultProjectParallel(
		IterableInterval out,
		RandomAccessibleInterval in,
		UnaryComputerOp method,
		int dim)
	(RealType out?) =
	net.imagej.ops.stats.DefaultMean(
		RealType out?,
		Iterable in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.deconvolve.NonCirculantFirstGuess(
		RandomAccessibleInterval in,
		RealType outType,
		Dimensions k)
	(RandomAccessibleInterval arg) =
	net.imagej.ops.deconvolve.NonCirculantNormalizationFactor(
		RandomAccessibleInterval arg,
		Dimensions k,
		Dimensions l,
		RandomAccessibleInterval fftInput,
		RandomAccessibleInterval fftKernel)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.FFTMethodsLinearFFTFilterC(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		RandomAccessibleInterval fftInput?,
		RandomAccessibleInterval fftKernel?,
		boolean performInputFFT?,
		boolean performKernelFFT?,
		BinaryComputerOp frequencyOp)
	(IterableInterval out) =
	net.imagej.ops.filter.addPoissonNoise.AddPoissonNoiseMap(
		IterableInterval out,
		IterableInterval in)
	(RandomAccessibleInterval out) =
	net.imagej.ops.filter.convolve.ConvolveFFTC(
		RandomAccessibleInterval out,
		RandomAccessibleInterval in1,
		RandomAccessibleInterval in2,
		RandomAccessibleInterval fftInput?,
		RandomAccessibleInterval fftKernel?,
		boolean performInputFFT?,
		boolean performKernelFFT?)
	(IterableInterval out) =
	net.imagej.ops.filter.max.DefaultMaxFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.filter.mean.DefaultMeanFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.filter.median.DefaultMedianFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.filter.min.DefaultMinFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(IterableInterval out) =
	net.imagej.ops.filter.sigma.DefaultSigmaFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		Double range,
		Double minPixelFraction)
	(IterableInterval out) =
	net.imagej.ops.filter.variance.DefaultVarianceFilter(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.image.integral.WrappedIntegralImg(
		RandomAccessibleInterval in)
	(IterableInterval arg) =
	net.imagej.ops.map.MapIIAndIIInplace(
		IterableInterval arg,
		IterableInterval in,
		BinaryInplaceOp op)
	(Iterable arg) =
	net.imagej.ops.map.MapIterableInplace(
		Iterable arg,
		UnaryInplaceOp op)
	(Iterable out) =
	net.imagej.ops.map.MapNullaryIterable(
		Iterable out,
		NullaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.map.neighborhood.DefaultMapNeighborhood(
		IterableInterval out,
		RandomAccessibleInterval in1,
		Shape in2,
		UnaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.math.multiply.ComplexConjugateMultiplyMap(
		IterableInterval out,
		IterableInterval in1,
		IterableInterval in2)
	(ComplexType out) =
	net.imagej.ops.math.multiply.ComplexConjugateMultiplyOp(
		ComplexType out,
		ComplexType in1,
		ComplexType in2)
	(IterableInterval out?) =
	net.imagej.ops.morphology.dilate.ListDilate(
		IterableInterval out?,
		RandomAccessibleInterval in1,
		List in2,
		boolean isFull?)
	(IterableInterval out?) =
	net.imagej.ops.morphology.erode.ListErode(
		IterableInterval out?,
		RandomAccessibleInterval in1,
		List in2,
		boolean isFull?)
	(IterableInterval out) =
	net.imagej.ops.threshold.localMean.LocalMeanThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c)
	(IterableInterval out) =
	net.imagej.ops.threshold.localNiblack.LocalNiblackThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c,
		double k)
	(IterableInterval out) =
	net.imagej.ops.threshold.localPhansalkar.LocalPhansalkarThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double k?,
		double r?)
	(IterableInterval out) =
	net.imagej.ops.threshold.localSauvola.LocalSauvolaThreshold(
		IterableInterval out,
		RandomAccessibleInterval in,
		Shape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double k?,
		double r?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.transform.crop.CropRAI(
		RandomAccessibleInterval in1,
		Interval in2,
		boolean dropSingleDimensions?)
	(IterableInterval out) =
	net.imagej.ops.transform.project.ProjectRAIToII(
		IterableInterval out,
		RandomAccessibleInterval in,
		UnaryComputerOp method,
		int dim)
	(IterableInterval out) =
	net.imagej.ops.transform.project.ProjectRAIToIterableInterval(
		IterableInterval out,
		RandomAccessibleInterval in,
		UnaryComputerOp method,
		int dim)
	(Iterable out) =
	net.imagej.ops.map.MapIterableToIterable(
		Iterable out,
		Iterable in,
		UnaryComputerOp op)
	(IterableInterval out) =
	net.imagej.ops.threshold.localMean.LocalMeanThresholdIntegral(
		IterableInterval out,
		RandomAccessibleInterval in,
		RectangleShape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c)
	(IterableInterval out) =
	net.imagej.ops.threshold.localNiblack.LocalNiblackThresholdIntegral(
		IterableInterval out,
		RandomAccessibleInterval in,
		RectangleShape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double c,
		double k)
	(IterableInterval out) =
	net.imagej.ops.threshold.localPhansalkar.LocalPhansalkarThresholdIntegral(
		IterableInterval out,
		RandomAccessibleInterval in,
		RectangleShape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double k?,
		double r?)
	(IterableInterval out) =
	net.imagej.ops.threshold.localSauvola.LocalSauvolaThresholdIntegral(
		IterableInterval out,
		RandomAccessibleInterval in,
		RectangleShape shape,
		OutOfBoundsFactory outOfBoundsFactory?,
		double k?,
		double r?)
	(RandomAccessibleInterval out) =
	net.imagej.ops.math.ConstantToIIOutputRAI$Add(
		RandomAccessibleInterval out,
		IterableInterval in,
		NumericType value)
	(RandomAccessibleInterval out) =
	net.imagej.ops.math.ConstantToIIOutputRAI$Divide(
		RandomAccessibleInterval out,
		IterableInterval in,
		NumericType value)
	(RandomAccessibleInterval out) =
	net.imagej.ops.math.ConstantToIIOutputRAI$Multiply(
		RandomAccessibleInterval out,
		IterableInterval in,
		NumericType value)
	(RandomAccessibleInterval out) =
	net.imagej.ops.math.ConstantToIIOutputRAI$Subtract(
		RandomAccessibleInterval out,
		IterableInterval in,
		NumericType value)
	net.imagej.ops.thread.chunker.ChunkerInterleaved(
		Chunk chunkable,
		long numberOfElements)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.distancetransform.DefaultDistanceTransform(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in)
	(RandomAccessibleInterval out?) =
	net.imagej.ops.image.distancetransform.DefaultDistanceTransformCalibration(
		RandomAccessibleInterval out?,
		RandomAccessibleInterval in,
		double[] calibration)
