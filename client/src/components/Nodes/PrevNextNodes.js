import React from 'react'
import NodesGroup from './NodesGroup'

const PrevNodes = ( {nodesPrev, nodesNext} ) => {
	return (
		<div className="col">
			<NodesGroup nodes={nodesNext} title="Next"/>
			<NodesGroup nodes={nodesPrev} title="Prev"/>
		</div>
	)
}

export default PrevNodes
