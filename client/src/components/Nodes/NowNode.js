import React from 'react'
import Node from './Node'

const NowNode = ( {node} ) => {
	return (
		<div className="col-5">
			<Node node={node}/>
		</div>
	)
}

export default NowNode
